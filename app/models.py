"Database models for the application."

from app import db
from datetime import datetime
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declared_attr

class Permissions:
    # save bibliography items to a list:
    SAVE_TO_LIST = 1
    EDIT_BIBLIOGRAPHY = 2
    ADMIN = 4


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
        return f'<Role {self.name}>'


class User(db.Model):
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


class Lock:
    '''Class mix-in for record locking.

Helps prevent simultaneous record access for modification
in order to avoid data inconsistency.'''

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
    'subjects_collectivities',
    db.Column('document_id', db.Integer,
              db.ForeignKey('documents.document_id'), nullable=False),
    db.Column('collectivities_id', db.Integer,
              db.ForeignKey('collectivities.id'), nullable=False)
)


class Language(db.Model, Lock):
    __tablename__ = 'languages'

    language_id = db.Column(db.Integer, primary_key=True)
    language_name = db.Column(db.String(45), nullable=False)
    native_name = db.Column(db.String(45))
    other_name = db.Column(db.String(45))
    iso_639_1_language_code = db.Column(db.String(5))
    iso_639_2_language_code = db.Column(db.String(3))


class Document(db.Model, Lock):
    __tablename__ = 'documents'

    document_id = db.Column(db.Integer, primary_key=True)
    document_type_id = db.Column(
        db.Integer, db.ForeignKey('document_types.type_id'))

    #document_type = db.relationship()

    language_id = db.Column(
        db.Integer, db.ForeignKey('languages.language_id'))
    original_language_id = db.Column(
        db.Integer, db.ForeignKey('languages.language_id'))

    language = db.relationship(
        'Language',
        backref='documents',
        foreign_keys=[language_id])
    original_language = db.relationship(
        'Language', backref='documents_original_lang',
        foreign_keys=[original_language_id])

    collectivity_subjects = db.relationship(
        'CollectiveBody',
        secondary=subjects_collectivities,
        backref=db.backref('subjects_collectivities', lazy='dynamic'),
        lazy='dynamic')

    _master_doc = association_proxy('master_document', 'dependent_doc')
    _dependent_docs = association_proxy('dependent_docs', 'master_doc')

    responsibility_collectivities = db.relationship(
        'ResponsibilityCollectivity',
        back_populates='document')

    title_proper = db.Column(db.String(255))
    parallel_title = db.Column(db.String(255))
    other_title_inf = db.Column(db.String(255))
    edition_statement = db.Column(db.String(40))
    parallel_edition_stmt = db.Column(db.String(40))

    # text field length:
    # Model.column.property.columns[0].type.length

    additional_edition_stmt = db.Column(db.String(40))
    numbering = db.Column(db.String(70))
    publication_date = db.Column(db.String(10))
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


class DocumentType(db.Model, Lock):
    __tablename__ = 'document_types'

    # default types shall be:
    # Book, Article, Periodical, Series

    type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    description = db.Column(db.String(200))


class CollectiveBody(db.Model, Lock):
    __tablename__ = 'collectivities'

    responsibility_collectivities = db.relationship(
        'ResponsibilityCollectivity',
        back_populates='collectivity')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(200))
    abbr = db.Column(db.String(45))
    description = db.Column(db.String(200))


class ResponsibilityName(db.Model, Lock):
    __tablename__ = 'responsibility_names'

    responsibility_collectivities = db.relationship(
        'ResponsibilityCollectivity',
        back_populates='responsibility')

    id = db.Column(db.Integer, primary_key=True)
    responsibility_name = db.Column(db.String(45), nullable=False)
    responsibility_abbr = db.Column(db.String(6))
    modifiable = db.Column(db.Boolean, default=True)


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
    ordering = db.Column(db.Integer)

    #jak nie będzie działało, spróbować z back_populates
    responsibility = db.relationship(
        'ResponsibilityName', back_populates='responsibility_collectivities')
    collectivity = db.relationship(
        'CollectiveBody', back_populates='responsibility_collectivities')
    document = db.relationship(
        'Document', back_populates='responsibility_collectivities')


class Keyword(db.Model, Lock):
    __tablename__ = 'keywords'

    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(70), nullable=False)
    determiner = db.Column(db.String(45))


# subject_keywords


class GeographicLocation(db.Model, Lock):
    __tablename__ = 'geographic_locations'

    location_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    name_variant = db.Column(db.String(45))
    determiner = db.Column(db.String(45))
    note = db.Column(db.String(100))


# subject_locations


class Person(db.Model, Lock):
    __tablename__ = 'people'

    person_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(68))
    last_name = db.Column(db.String(68))
    note = db.Column(db.String(200))
    life_years = db.Column(db.String(14))
    birth_date = db.Column(db.Date)
    death_date = db.Column(db.Date)


class PersonNameVariant(db.Model, Lock):
    __tablename__ = 'person_name_variants'

    individual_id = db.Column(db.Integer, primary_key=True)
    first_name_variant = db.Column(db.String(68))
    last_name_variant = db.Column(db.String(68))
    variant_notes = db.Column(db.String(45))


# subjects_people


# responsibilities_people


class RelatedDocuments(db.Model, Lock):
    "Self-referential relationship table for the documents table."

    __tablename__ = 'related_documents'
    __table_args__ = (db.UniqueConstraint(
        'master_doc_id', 'dependent_doc_id'),)

    master_doc_id = db.Column(
        db.Integer, db.ForeignKey('documents.document_id'), primary_key=True)
    dependent_doc_id = db.Column(
        db.Integer, db.ForeignKey('documents.document_id'), primary_key=True)
    description = db.Column(db.String(45))
    ordering = db.Column(db.Integer, default=0)

    dependent_doc = db.relationship(
        'Document',
        primaryjoin=(dependent_doc_id == Document.document_id),
        backref='master_document')
    master_doc = db.relationship(
        'Document',
        primaryjoin=(master_doc_id == Document.document_id),
        backref='dependent_docs')
