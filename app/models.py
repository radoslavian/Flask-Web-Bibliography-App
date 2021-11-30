'''Database models for the application.

Portions of the code (when specified in the docstring/comments)
are adapted from:
Miguel Grinberg, Flask Web Development, [Beijing etc.], 2018.
'''

__name__ = 'models'
__all__ = ['Permissions', 'Role', 'User', 'AnonymousUser', 'Language',
           'Document', 'DocumentType', 'CollectiveBody', 'ResponsibilityName',
           'ResponsibilityCollectivity','Keyword', 'GeographicLocation',
           'Person', 'ResponsibilityPerson', 'PersonNameVariant',
           'RelatedDocuments']

from app import db#, login_manager
from datetime import datetime
from flask import current_app
from flask_login import UserMixin, AnonymousUserMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declared_attr
from werkzeug.security import generate_password_hash, check_password_hash
from app.search import add_to_index, remove_from_index, query_index

# COLLATION = 'utf8_general_ci'

class SearchableMixin(object):
    '''Reused from: M. Grinberg, Flask Mega Tutorial.
    https://blog.miguelgrinberg.com/
    '''
    @property
    def id(self):
        return getattr(self, self.__primary_key__)

    @classmethod
    def search(cls, expression, page, per_page):
        ids, total = query_index(cls.__tablename__,
                                 expression, page, per_page)
        if total == 0 or not ids:
            return cls.query.filter(
                getattr(cls, cls.__primary_key__) == 0), 0
        when = []
        for i in range(len(ids)):
            when.append((ids[i], i))
        return cls.query.filter(
            getattr(cls, cls.__primary_key__).in_(ids)).order_by(
            db.case(when, value=getattr(cls, cls.__primary_key__))), total

    @classmethod
    def before_commit(cls, session):
        session._changes = {
            'add': list(session.new),
            'update': list(session.dirty),
            'delete': list(session.deleted)
        }

    @classmethod
    def after_commit(cls, session):
        for obj in session._changes['add']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['update']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['delete']:
            if isinstance(obj, SearchableMixin):
                remove_from_index(obj.__tablename__, obj)
        session._changes = None

    @classmethod
    def reindex(cls):
        for obj in cls.query:
            add_to_index(cls.__tablename__, obj)

db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)


class Permissions:
    # permission to save bibliography items to a list:
    SAVE_TO_LIST = 1
    EDIT_BIBLIOGRAPHY = 2
    ADMIN = 4 # += activate/modify user accounts


class Role(db.Model):
    __tablename__ = 'roles'

    role_id = db.Column(db.Integer, unique=True, nullable=False,
                        primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    @staticmethod
    def insert_roles():
        '''Inserts roles in the database.

        New role objects are only created for roles that are not already
        present in the database. This way the list can be updated
        in the future when changes need to be made.
        Adapted from: M. Grinberg...
        '''
        roles = {
            'User': [Permissions.SAVE_TO_LIST],
            'Editor': [Permissions.SAVE_TO_LIST,
                       Permissions.EDIT_BIBLIOGRAPHY],
            'Administrator:': [Permissions.SAVE_TO_LIST,
                               Permissions.EDIT_BIBLIOGRAPHY,
                               Permissions.ADMIN]
        }
        default_role = 'User'

        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions += perm

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm

    def __repr__(self):
        return f'<Role: {self.name}>'


class User(UserMixin, db.Model):
    '''User representation in the application.
    Solutions adapted from: M. Grinberg...
    '''
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    email = db.Column(db.String(45))
    name = db.Column(db.String(64))
    username = db.Column(db.String(45))
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    member_since = db.Column(db.DateTime, default=datetime.utcnow)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['APP_ADMIN']:
                self.role = Role.query.filter_by(name='Administrator').first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def can(self, perm):
        return self.role is not None and self.role.has_permission(perm)

    def is_administrator(self):
        return self.can(Permissions.ADMIN)


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False


#login_manager.anonymous_user = AnonymousUser


class Lock:
    '''A mix-in class for record locking.

    Helps prevent simultaneous record access for modification
    in order to avoid data inconsistency.
    '''
    locked = db.Column(db.Boolean, default=False)
    lock_timestamp = db.Column(db.DateTime)

    @declared_attr
    def _locking_user_id(cls):
        return db.Column(db.Integer, db.ForeignKey('users.user_id'))

    @declared_attr
    def locking_user(cls):
        return db.relationship('User')

    def __commit(self):
        db.session.add(self)
        db.session.commit()

    def lock(self, user):
        if not self.locked:
            self.locked = True
            self.locking_user = user
            self.lock_timestamp = datetime.utcnow()
            self.__commit()

    def unlock(self):
        if self.locked:
            self.locked = False
            self.locking_user = None
            self.lock_timestamp = None
            self.__commit()


subjects_collectivities = db.Table(
    'subjects_collectivities_join',
    db.Column('document_id', db.Integer,
              db.ForeignKey('documents.document_id'), nullable=False),
    db.Column('collectivity_id', db.Integer,
              db.ForeignKey('collectivities.id'), nullable=False),
    db.PrimaryKeyConstraint('document_id', 'collectivity_id'),
    db.UniqueConstraint('document_id', 'collectivity_id')
)


subjects_languages = db.Table(
     'subjects_languages_join',
    db.Column('document_id', db.Integer,
              db.ForeignKey('documents.document_id'), nullable=False),
    db.Column('language_id', db.Integer,
              db.ForeignKey('languages.language_id'), nullable=False),
    db.PrimaryKeyConstraint('document_id', 'language_id'),
    db.UniqueConstraint('document_id', 'language_id')
)


class Language(db.Model, Lock, SearchableMixin):
    __tablename__ = 'languages'
    __primary_key__ = 'language_id'
    __table_args__ = (db.UniqueConstraint(
        'language_name', 'iso_639_1_language_code',
        'iso_639_2_language_code'),)

    # searchable fields (for Elasticsearch or other engines)
    __searchable__ = ['language_name', 'native_name']

    language_id = db.Column(db.Integer, primary_key=True)
    language_name = db.Column(db.String(64),
                              nullable=False, index=True)
    native_name = db.Column(db.String(64), index=True)
    other_name = db.Column(db.String(64))
    iso_639_1_language_code = db.Column(db.String(5))
    iso_639_2_language_code = db.Column(db.String(3))

    @staticmethod
    def add_languages(number=0):
        '''Adds English (only) language names to the database from
        a pycountry dataset.
        '''
        import pycountry
        i = 0

        for language in pycountry.languages:
            if Language.query.filter_by(
                    language_name=language.name).first() is None:
                iso_639_1_code = getattr(language, 'alpha_2', None)
                iso_639_2_code = getattr(language, 'alpha_3', None)
                db.session.add(Language(
                    language_name=language.name,
                    iso_639_1_language_code=iso_639_1_code,
                    iso_639_2_language_code=iso_639_2_code))
                if number:
                    if i > number: break
                    i += 1
        db.session.commit()

    def __repr__(self):
        return f'Language: <{self.language_name}>'

    def __str__(self):
        output = self.language_name
        if self.native_name:
            output += ' - ' + self.native_name
        # one out of the two
        if self.iso_639_1_language_code:
            output += ' (' + self.iso_639_1_language_code + ')'
        elif self.iso_639_2_language_code:
            output += ' (' + self.iso_639_2_language_code + ')'
        return output

    def __html__(self):
        return self.__str__()


class Document(db.Model, Lock, SearchableMixin):
    __primary_key__ = 'document_id'
    __tablename__ = 'documents'
    __searchable__ = ['title_proper', 'parallel_title', 'series']

    document_id = db.Column(db.Integer, primary_key=True)
    document_type_id = db.Column(
        db.Integer, db.ForeignKey('document_types.type_id'))
    language_id = db.Column(
        db.Integer, db.ForeignKey('languages.language_id'))
    original_language_id = db.Column(
        db.Integer, db.ForeignKey('languages.language_id'))
    title_proper = db.Column(db.String(255), index=True)
    parallel_title = db.Column(db.String(255))
    other_title_inf = db.Column(db.String(255))
    edition_statement = db.Column(db.String(40))
    parallel_edition_stmt = db.Column(db.String(40))

    # how to get text field length:
    # Model.column.property.columns[0].type.length

    additional_edition_stmt = db.Column(db.String(40))
    numbering = db.Column(db.String(70))
    publication_date = db.Column(db.String(10))

    # for searching purposes
    # view page shall give hints about using each of
    # the two fields.
    # publication_year = db.Column(db.Integer)
    pagination = db.Column(db.String(30))
    physical_details = db.Column(db.String(45))
    dimensions = db.Column(db.String(60))
    accompanying_material = db.Column(db.String(60))

    # for more rudimentary series; separate relationship
    # for series defined as a document

    series = db.Column(db.String(45))
    note = db.Column(db.String(5000))
    issn = db.Column(db.String(9))
    isbn_10 = db.Column(db.String(13))
    isbn_13 = db.Column(db.String(17))

    document_type = db.relationship(
        'DocumentType',
        backref=db.backref('documents', lazy='dynamic'))
    responsibility_collectivities = db.relationship(
        'ResponsibilityCollectivity',
        back_populates='document',
        cascade='all, delete-orphan')
    responsibilities_people = db.relationship(
        'ResponsibilityPerson',
        back_populates='document',
        cascade='all, delete-orphan')
    language = db.relationship(
        'Language',
        backref=db.backref('documents', lazy='dynamic'),
        foreign_keys=[language_id])
    original_language = db.relationship(
        'Language',
        backref=db.backref('documents_original_lang', lazy='dynamic'),
        foreign_keys=[original_language_id])
    publication_places = db.relationship(
        'GeographicLocation',
        secondary='publication_places_join',
        backref=db.backref('document_publication_place',
                           lazy='dynamic'),
        lazy='dynamic')
    collectivity_subjects = db.relationship(
        'CollectiveBody',
        secondary='subjects_collectivities_join',
        backref=db.backref('documents_topics', lazy='dynamic'),
        lazy='dynamic')
    language_subjects = db.relationship(
        'Language',
        secondary='subjects_languages_join',
        backref=db.backref('documents_topics', lazy='dynamic'),
        lazy='dynamic'
    )
    keywords = db.relationship(
        'Keyword',
        secondary='subject_keywords',
        backref=db.backref('documents', lazy='dynamic'),
        lazy='dynamic')
    topic_people = db.relationship(
        'Person',
        secondary='topic_people_join',
        backref=db.backref('documents_topics', lazy='dynamic'),
        lazy='dynamic')
    subjects_locations = db.relationship(
        'GeographicLocation',
        secondary='subjects_locations_join',
        backref=db.backref('documents_topics', lazy='dynamic'),
        lazy='dynamic')

    _master_doc = association_proxy('master_document', 'dependent_doc')
    _dependent_docs = association_proxy('dependent_docs', 'master_doc')

    def __repr__(self):
        output = f'Document: {self.title_proper}'
        if self.document_type: output += f' ({self.document_type.name})'
        return '<' + output + '>'

    def __str__(self):
        output = self.title_proper
        if self.parallel_title:
            output += ' : ' + self.parallel_title
        if self.other_title_inf:
            output += ' : ' + self.other_title_inf
        if self.publication_date:
            output += ' . - ' + self.publication_date
        return output

    def __html__(self):
        return self.__str__()


class DocumentType(db.Model, Lock):
    __tablename__ = 'document_types'

    # default types shall be:
    # Book, Article, Periodical, Series

    type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False) # + unique
    description = db.Column(db.String(200))
    modifiable = db.Column(db.Boolean, default=True)

    @staticmethod
    def add_basic_document_types():
        document_types = ['book', 'article', 'periodical', 'series']

        for document_type in document_types:
            doc_type = DocumentType.query.filter_by(
                name=document_type).first()
            if not doc_type:
                db.session.add(DocumentType(name=document_type,
                                            modifiable=False))
                db.session.commit()

    def __repr__(self):
        return f'<Document type: {self.name}>'


class CollectiveBody(db.Model, Lock, SearchableMixin):
    '''Model for collective bodies.
    These include (among others): organisations, companies,
    events, publishers.
    '''
    __primary_key__ = 'id'
    __tablename__ = 'collectivities'
    __searchable__ = ['name', 'address']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, nullable=False)
    address = db.Column(db.String(200))
    abbr = db.Column(db.String(45))
    description = db.Column(db.String(200))

    responsibilities = db.relationship(
        'ResponsibilityCollectivity',
        back_populates='collectivity',
        cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Collective body: {self.name}>'

    def __str__(self):
        return self.name

    def __html__(self):
        return self.__str__()


class ResponsibilityName(db.Model, Lock, SearchableMixin):
    '''Entity's (individual, organisation) responsibility/function name in
    the document (author, editor, publisher etc.)
    '''
    __tablename__ = 'responsibility_names'

    id = db.Column(db.Integer, primary_key=True)
    responsibility_name = db.Column(
        db.String(45), nullable=False, index=True) # + unique, nullable=False
    responsibility_abbr = db.Column(db.String(6))
    modifiable = db.Column(db.Boolean, default=True)

    responsibility_collectivities = db.relationship(
        'ResponsibilityCollectivity',
        back_populates='responsibility',
        cascade='all, delete-orphan',
        lazy='dynamic')
    responsibilities_people = db.relationship(
        'ResponsibilityPerson',

        # czy tu też nie powinno być:
        # cascade='all, delete-orphan'
        back_populates='responsibility',
        lazy='dynamic')

    @staticmethod
    def add_basic_responsibilities():
        responsibilities = ['afterword', 'author', 'editor',
                            'editor in chief', 'graphic designer',
                            'illustrator', 'proofreader', 'publisher',
                            'publishing house', 'translator', 'unspecified']

        for responsibility in responsibilities:
            responsibility_name = ResponsibilityName.query.filter_by(
                responsibility_name=responsibility).first()
            if not responsibility_name:
                db.session.add(ResponsibilityName(
                    responsibility_name=responsibility, modifiable=False))
                db.session.commit()

    def __repr__(self):
        return f'<Document responsibility: {self.responsibility_name}>'

class ResponsibilityCollectivity(db.Model):
    '''Three entity association table for collective bodies
    holding responsibilities (authorship etc.) in a document.
    '''
    __tablename__ = 'responsibilities_collectivities'
    __table_args__ = (db.UniqueConstraint(
        'responsibility_id', 'collectivity_id', 'document_id'),)

    id = db.Column(db.Integer, primary_key=True)
    responsibility_id = db.Column(
        db.Integer, db.ForeignKey('responsibility_names.id'),
        nullable=False)
    collectivity_id = db.Column(
        db.Integer, db.ForeignKey('collectivities.id'),
        nullable=False)
    document_id = db.Column(
        db.Integer, db.ForeignKey('documents.document_id'),
        nullable=False)
    ordering = db.Column(db.SmallInteger, default=0)

    responsibility = db.relationship(
        'ResponsibilityName', back_populates='responsibility_collectivities')
    collectivity = db.relationship(
        'CollectiveBody', back_populates='responsibilities')
    document = db.relationship(
        'Document', back_populates='responsibility_collectivities')


class Keyword(db.Model, Lock, SearchableMixin):
    __tablename__ = 'keywords'
    __table_args__ = (db.UniqueConstraint('keyword', 'determiner'),)
    __searchable__ = ['keyword']
    __primary_key__ = 'id'

    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(70), nullable=False, index=True)
    determiner = db.Column(db.String(45))

    def __repr__(self):
        return f'<Keyword: {self.keyword}>'

    def __str__(self):
        output = self.keyword
        if self.determiner:
            output += ' (' + self.determiner + ')'
        return output

    def __html__(self):
        return self.__str__()


subjects_keywords = db.Table(
    'subject_keywords',
    db.Column('document_id', db.Integer,
              db.ForeignKey('documents.document_id'), nullable=False),
    db.Column('keyword_id', db.Integer,
              db.ForeignKey('keywords.id'), nullable=False,),
    db.PrimaryKeyConstraint('document_id', 'keyword_id', name='subject_pk'),
    db.UniqueConstraint('document_id', 'keyword_id')
)


publication_places = db.Table(
    'publication_places_join',
    db.Column('place_id', db.Integer,
              db.ForeignKey('geographic_locations.location_id'),
              nullable=False),
    db.Column('document_id', db.Integer,
              db.ForeignKey('documents.document_id'), nullable=False),
    db.PrimaryKeyConstraint('place_id', 'document_id'),
    db.UniqueConstraint('place_id', 'document_id')
)


class GeographicLocation(db.Model, Lock, SearchableMixin):
    '''Model for geographic names (cities, states etc.)
    '''
    __primary_key__ = 'location_id'
    __tablename__ = 'geographic_locations'
    __searchable__ = ['name', 'native_name', 'other_name']

    location_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False, index=True)
    native_name = db.Column(db.String(45), index=True)
    other_name = db.Column(db.String(45))
    determiner = db.Column(db.String(45))
    note = db.Column(db.String(100))

    def __repr__(self):
        return f'<{self.name}>'

    def __str__(self):
        output = self.name
        if self.other_name:
            output += ' (' + self.other_name + ')'
        elif self.native_name:
            output += ' (' + self.native_name + ')'
        return output

    def __html__(self):
        return self.__str__()


subjects_locations = db.Table(
    'subjects_locations_join',
    db.Column('document_id', db.Integer,
              db.ForeignKey('documents.document_id'), nullable=False),
    db.Column('location_id', db.Integer,
              db.ForeignKey('geographic_locations.location_id'),
              nullable=False),
    db.UniqueConstraint('document_id', 'location_id'),
    db.PrimaryKeyConstraint('document_id', 'location_id')
)


class Person(db.Model, Lock, SearchableMixin):
    __primary_key__ = 'person_id'
    __tablename__ = 'people'
    __searchable__ = ['forenames', 'last_name']

    person_id = db.Column(db.Integer, primary_key=True)
    forenames = db.Column(db.String(68)) # name and/or second name
    last_name = db.Column(db.String(68), index=True)
    note = db.Column(db.String(200))
    life_years = db.Column(db.String(14))
    birth_date = db.Column(db.Date)
    death_date = db.Column(db.Date)

    responsibilities = db.relationship(
        'ResponsibilityPerson',
        back_populates='person')
    name_variants = db.relationship(
        'PersonNameVariant',
        backref=db.backref('person'), lazy='dynamic')

    def __repr__(self):
        return f'<Person name: {self.forenames} {self.last_name}>'

    def __str__(self):
        output = f'{self.last_name}'
        if self.forenames:
            output += f', {self.forenames}'
        if self.life_years:
            output += f' ({self.life_years})'
        return output

    def __html__(self):
        output = f'<em>{self.last_name}</em>'
        if self.forenames:
            output += f', {self.forenames}'
        if self.life_years:
            output += f' ({self.life_years})'
        return output


class ResponsibilityPerson(db.Model):
    __tablename__ = 'responsibilities_people'
    __table_args__ = (db.UniqueConstraint(
        'responsibility_id', 'person_id', 'document_id'),)

    id = db.Column(db.Integer, primary_key=True)
    responsibility_id = db.Column(
        db.Integer, db.ForeignKey('responsibility_names.id'),
        nullable=False)
    person_id = db.Column(
        db.Integer, db.ForeignKey('people.person_id'),
        nullable=False)
    document_id = db.Column(
        db.Integer, db.ForeignKey('documents.document_id'),
        nullable=False)
    ordering = db.Column(db.SmallInteger, default=0)

    responsibility = db.relationship(
        'ResponsibilityName',
        back_populates='responsibilities_people')
    person = db.relationship(
        'Person', back_populates='responsibilities')
    document = db.relationship(
        'Document', back_populates='responsibilities_people')


class PersonNameVariant(db.Model, Lock, SearchableMixin):
    __primary_key__ = 'variant_id'
    __tablename__ = 'person_name_variants'
    __searchable__ = ['first_name_variant', 'last_name_variant']

    variant_id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('people.person_id'))
    first_name_variant = db.Column(db.String(68))
    last_name_variant = db.Column(db.String(68), index=True)
    variant_notes = db.Column(db.String(45))

    def __repr__(self):
        return f'<Person name variant: \
{self.first_name_variant} {self.last_name_variant}>'

    def __html__(self):
        output = ''
        if self.last_name_variant:
            output += f'<em>{self.last_name_variant}</em>'
        if self.first_name_variant:
            output += f', {self.first_name_variant}'
        return f'''<span class="name-variant">{output} &#8594;
        {str(self.person)}</span>'''


topic_people = db.Table(
    'topic_people_join',
    db.Column('document_id', db.Integer,
              db.ForeignKey('documents.document_id'), nullable=False),
    db.Column('person_id', db.Integer,
              db.ForeignKey('people.person_id'), nullable=False),
    db.UniqueConstraint('document_id', 'person_id'),
    db.PrimaryKeyConstraint('document_id', 'person_id')
)


class RelatedDocuments(db.Model):
    '''Self-referential relationship table for the documents table.
    '''
    __tablename__ = 'related_documents'
    __table_args__ = (db.UniqueConstraint(
        'master_doc_id', 'dependent_doc_id'),)

    id = db.Column(db.Integer, primary_key=True)
    master_doc_id = db.Column(
        db.Integer, db.ForeignKey('documents.document_id'),
        nullable=False)
    dependent_doc_id = db.Column(
        db.Integer, db.ForeignKey('documents.document_id'),
        nullable=False)
    description = db.Column(db.String(45))
    ordering = db.Column(db.SmallInteger, default=0)

    dependent_doc = db.relationship(
        'Document',
        primaryjoin=(dependent_doc_id == Document.document_id),
        backref=db.backref('master_document', uselist=False,
                           cascade='all, delete-orphan'))
    master_doc = db.relationship(
        'Document',
        primaryjoin=(master_doc_id == Document.document_id),
        backref=db.backref('dependent_docs', cascade='all, delete-orphan'),
        uselist=False)
