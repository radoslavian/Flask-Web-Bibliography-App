from app import db
from sys import stderr
import json
from ..models import *
from flask import request, flash
from flask_wtf import FlaskForm
from sqlalchemy.exc import IntegrityError
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms import (StringField, SubmitField, TextAreaField, HiddenField,
                     SelectMultipleField, BooleanField, ValidationError,
                     validators)
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, Regexp
from app.utils.helpers import length


class QuickSearchForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args

        if 'csrf_enabled' not in kwargs:
            kwargs['meta'] = {'csrf': False}
        super(QuickSearchForm, self).__init__(*args, **kwargs)

    q = StringField(validators=[validators.DataRequired()],
                    render_kw={'class': 'form-control w-75',
                               'placeholder': 'Full text quick-search',
                               'data-toggle': 'tooltip',
                               'size': 40,
                               'title': '''Search for documents,
			       personal/geographic/
			       collective names and subject keywords.'''})
    search = SubmitField('Search', render_kw={
        'class': 'btn btn-success my-2 my-sm-0'})


class EditProfileForm(FlaskForm):
    '''User profile edit form.
    Adapted from: M. Grinberg...
    '''
    def __init__(self, user, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.user = user

    def validate_email(self, field):
        if (field.data != self.user.email and
            User.query.filter_by(email=field.data).first()):
            raise ValidationError('Email already registered!')

    def validate_username(self, field):
        if (field.data != self.user.username and
            User.query.filter_by(username=field.data).first()):
            raise ValidationError('Username already in use!')

    email = StringField('User email:', validators=[
        DataRequired(), Length(1, length(User.email)), Email()])
    username = StringField(
        'Username:',
        validators=[
            DataRequired(), Length(0, length(User.name),
            Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                   'Only letters, underscores, numbers and dots are allowed'
                   ' in the username.'))])
    name = StringField('Real name:',
                       validators=[Length(0, length(User.name))])
    confirmed = BooleanField('Confirmed')
    role = QuerySelectField('Role:', query_factory=lambda: Role.query,
                            get_label=lambda role: role.name.capitalize())
    submit = SubmitField('Submit')


class ModelEditForm(FlaskForm):
    '''Abstract class for entity editing forms.
    Form fields should have the same names as attributes
    in the database model.
    '''
    submit = SubmitField()

    def __init__(self, *pargs, **kwargs):
        FlaskForm.__init__(self, *pargs, **kwargs)
        if 'obj' in kwargs:
            self.obj = kwargs.get('obj', None)
            self.submit.label.text = 'Update entity'
        else:
            self.submit.label.text = 'Create new'
        self.header = 'Edit Form Header'

    def redirect_to(self):
        '''Returns arguments for the url_for().
        '''
        pass

    def _commit(self):
        db.session.add(self.obj)
        try:
            db.session.commit()
        except IntegrityError as err:
            db.session.rollback()
            flash('Failed to perform operation due to '
                  'the data integrity error.')
            # to powinno iść do loga
            print(f'Failed to perform operation: {err}', file=stderr)
            return False
        else:
            flash(getattr(self, 'success_message', None)
                  or 'Successfully updated entry.')
            return True

    def commit_row(self):
        '''Shall be called from the commit_row method of
        the inheriting class in the following way (and order):
        super().commit_row()
        super()._commit()
        '''
        try:
            int(self.id.data)
        except ValueError:
            self.id.data = None
            self.obj = self.model()
            self.success_message = 'Successfully created new entry.'
        else:
            # self.obj = self.model.query.get(self.id.data)
            self.success_message = 'Entry successfully updated.'


class PersonEditForm(ModelEditForm):
    # klasa do poprawienia
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = Person
        if self.id.data:
            self.header = 'Update Person entry:'
        else:
            self.header = 'Create new Person entry:'
        self.get_variants()

    def validate_on_submit(self):
        # dokument też tak muszę ...
        if request.method == 'POST':
            return True
        else:
            return False

    def get_variants(self):
        '''Loads variants from object into the form.
        '''
        if getattr(self, 'obj', None):
            # id and variant text
            name_variants = [(variant.id, str(variant) +
                              f' (id {variant.id})')
                             for variant in self.obj.name_variants]
            self.name_variants.choices = name_variants

        elif self.name_variants.raw_data:
            for variant_id in self.name_variants.raw_data:
                if variant_id.isdigit():
                    variant = PersonNameVariant.query.get(int(variant_id))
                    if variant:
                        self.name_variants.choices.append(tuple(
                            [variant.variant_id, str(variant)]))
        self.name_variants.choices.sort()

    def add_variants(self):
        # adds to db
        if self.name_variants.raw_data:
            variants = []
            # takie samo jak w get_variants
            # jak to połączyć?
            for variant_id in self.name_variants.raw_data:
                if variant_id.isdigit():
                    variant = PersonNameVariant.query.get(int(variant_id))
                    if variant:
                        variants.append(variant)
            self.obj.name_variants = variants
        else:
            self.obj.name_variants = []

    def commit_row(self):
        super().commit_row()

        # poniższe el. do add_variants() mogą być w metodzie abs.
        # pobranie wartości do pól
        for field in ['forenames', 'last_name', 'note', 'life_years',
                      'birth_date', 'death_date']:
            value = getattr(self, field).data
            setattr(self.obj, field, value)

        self.add_variants()
        db.session.add(self.obj)
        return self._commit()

    id = HiddenField()
    forenames = StringField(
        'Forenames (first/second name):',
        render_kw={'required': 'required',
                   'maxlength': f'{length(Person.forenames)}'})
    last_name = StringField(
        'Last name:',
        render_kw={'maxlength': f'{length(Person.last_name)}'})
    note = TextAreaField(
        'Note:',
        render_kw={'maxlength': f'{length(Person.note)}'})
    life_years = StringField(
        'Life years (text format):',
        render_kw={'data-toggle': 'tooltip',
                   # Tooltip powinien być nad ikonką 'i' w kodzie szablonu
                   'title': '''Examples: 1923-2013; 1992-; [1992-]; 
                   any additional information should be put into notes.''',
                   'maxlength': f'{length(Person.life_years)}',
                   'pattern': '^[\d\-\[\]]+$'})
    birth_date = DateField('Exact birth date:')
    death_date = DateField('Exact expiration date:')
    name_variants = SelectMultipleField('Name Variants:', choices=[])
    submit = SubmitField(id='submit_form',
                         render_kw={'class': 'btn-block mt-1'})

    def redirect_to(self):
        return {'endpoint': 'main.person_details',
                'person_id': self.obj.id}


class BasicEditForm(ModelEditForm):
    def commit_row(self):
        super(BasicEditForm, self).commit_row()
        self.populate_obj(self.obj)
        return super(BasicEditForm, self)._commit()


class LanguageEditForm(BasicEditForm):
    def __init__(self, *pargs, **kwargs):
        super(LanguageEditForm, self).__init__(*pargs, **kwargs)
        self.model = Language
        if 'obj' in kwargs:
            self.header = 'Update Language entry:'
        else:
            self.header = 'Create new Language entry:'

    id = HiddenField()
    language_name = StringField('Language name:', validators=[
        DataRequired(),
        Length(1, length(Language.language_name))])
    native_name = StringField('Native language name:', validators=[
        Length(max=length(Language.native_name))])
    other_name = StringField('Other name:', validators=[
        Length(max=length(Language.other_name))])
    iso_639_1_language_code = StringField(
        'ISO-639-1 language code:', validators=[Length(max=2)])
    iso_639_2_language_code = StringField(
        'ISO-639-2 language code:', validators=[Length(max=3)])

    def redirect_to(self):
        return {'endpoint': 'main.language_details',
                'language_id': self.obj.id}


class DocumentTypeEditForm(BasicEditForm):
    def __init__(self, *pargs, **kwargs):
        super().__init__(*pargs, **kwargs)
        self.model = DocumentType
        if 'obj' in kwargs:
            self.header = 'Update Document Type entry entry:'
        else:
            self.header = 'Add new Document Type entry:'

    id = HiddenField()
    name = StringField(
        'Document type name:', validators=[
            DataRequired(),
            Length(max=length(DocumentType.name))])
    description = TextAreaField('Description:', validators=[
        Length(max=length(DocumentType.description))])

    def redirect_to(self):
        return {'endpoint': '.document_type',
                'type_id': self.obj.id}


class CollectiveBodyEditForm(BasicEditForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = CollectiveBody
        if 'obj' in kwargs:
            self.header = 'Update Collective Body entry:'
        else:
            self.header = 'Add new Collective Body entry:'

    id = HiddenField()
    name = StringField(
        'Collective body name:', validators=[
            DataRequired(),
            Length(max=length(CollectiveBody.name))])
    address = StringField(
        'Address:', validators=[
            Length(max=length(CollectiveBody.address))])
    abbr = StringField(
        'Formal abbreviation:',
        validators=[Length(max=length(CollectiveBody.abbr))])
    description = TextAreaField(
        'Description:',
        validators=[Length(max=length(CollectiveBody.description))])

    def redirect_to(self):
        return {'endpoint': 'main.collective_body_details',
                'c_body_id': self.obj.id}


class GeographicLocationEditForm(BasicEditForm):
    def __init__(self, *pargs, **kwargs):
        super().__init__(*pargs, **kwargs)
        self.model = GeographicLocation
        if 'obj' in kwargs:
            self.header = 'Update Geographic Location entry:'
        else:
            self.header = 'Create new Geographic Location entry:'

    id = HiddenField()
    name = StringField(
        'Name:', validators=[
            DataRequired(),
            Length(max=length(GeographicLocation.name))])
    native_name = StringField(
        'Native name:', validators=[
            Length(max=length(GeographicLocation.native_name))])
    other_name = StringField(
        'Other name:', validators=[
            Length(max=length(GeographicLocation.other_name))])
    determiner = StringField(
        'Determiner:', validators=[
            Length(max=length(GeographicLocation.determiner))])
    note = TextAreaField(
        'Note:', validators=[
            Length(max=length(GeographicLocation.note))])

    def redirect_to(self):
        return {'endpoint': 'main.geographic_location_details',
                'location_id': self.obj.id}


class KeywordEditForm(BasicEditForm):
    def __init__(self, *pargs, **kwargs):
        super().__init__(*pargs, **kwargs)
        self.model = Keyword
        if 'obj' in kwargs:
            self.header = 'Update Keyword (subject header) entry:'
        else:
            self.header = 'Create new Keyword (subject header) entry:'

    id = HiddenField()
    keyword = StringField(
        'Keyword:', validators=[
            DataRequired(),
            Length(max=length(Keyword.keyword))])
    determiner = StringField(
        'Determiner:', validators=[Length(max=length(Keyword.determiner))])

    def redirect_to(self):
        return {'endpoint': 'main.keyword_details',
                'keyword_id': self.obj.id}


class ResponsibilityNameEditForm(BasicEditForm):
    def __init__(self, *pargs, **kwargs):
        super().__init__(*pargs, **kwargs)
        self.model = ResponsibilityName
        if 'obj' in kwargs:
            self.header = 'Update Responsibility Name entry:'
        else:
            self.header = 'Create new Responsibility Name entry:'

    id = HiddenField()
    responsibility_name = StringField(
        'Responsibility name:', validators=[
            DataRequired(),
            Length(max=length(ResponsibilityName.responsibility_name))])
    responsibility_abbr = StringField(
        'Responsibility abbreviation:', validators=[
            Length(max=length(ResponsibilityName.responsibility_abbr))])

    def redirect_to(self):
        return {'endpoint': 'main.responsibility_details',
                'responsibility_id': self.obj.id}


class PersonNameVariantEditForm(BasicEditForm):
    def __init__(self, *pargs, **kwargs):
        super().__init__(*pargs, **kwargs)
        self.model = PersonNameVariant
        if 'obj' in kwargs:
            self.header = 'Update Person Name Variant entry:'
        else:
            self.header = 'Create new Person Name Variant entry:'

    id = HiddenField()
    first_name_variant = StringField(
        'First name:', validators=[
            Length(max=length(PersonNameVariant.first_name_variant))])
    last_name_variant = StringField(
        'Last name:', validators=[
            Length(max=length(PersonNameVariant.last_name_variant))])
    variant_notes = TextAreaField(
        'Notes:', validators=[
            Length(max=length(PersonNameVariant.variant_notes))])

    def redirect_to(self):
        return {'endpoint': 'main.name_variant',
                'variant_id': self.obj.id}


class DocumentEditForm(ModelEditForm):
    def __init__(self, *pargs, **kwargs):
        super().__init__(*pargs, **kwargs)
        self.model = Document
        if 'obj' in kwargs:
            self.header = 'Update Document entry:'
            self.load_stmts_of_responsibility_cbodies()
            self.load_stmts_of_responsibility_individuals()
            self.load_publication_places()
            self.load_collectivity_subjects()
            self.load_languages_as_subjects()
            self.load_keywords()
            self.load_topics_people()
            self.load_subjects_locations()
            self.load_dependent_documents()
        else:
            self.header = 'Create new Document entry:'

    def validate_on_submit(self):
        # rozwiązanie póki nie znajdę lepszego
        if request.method == 'POST':
            return True
        else:
            return False

    def commit_row(self):
        super(DocumentEditForm, self).commit_row()
        self.save_stmts_of_responsibility_coll_bodies()
        self.save_stmts_of_responsibility_individuals()
        self.save_document_language()
        self.save_original_language()
        self.save_publication_places()
        self.save_coll_bodies_as_subjects()
        self.save_languages_as_subjects()
        self.save_keywords()
        self.save_topics_people()
        self.save_subjects_locations()
        self.save_dependent_docs()
        self.save_text_fields()
        self.save_document_type()
        return self._commit()

    def load_stmts_of_responsibility(self, title_string, entity_dict,
                                     list_generator):
        '''General method for loading statements of responsibility.
        '''
        return [(json.dumps(entity_dict(entity)),
                 title_string(entity)) for entity in list_generator()]

    def load_stmts_of_responsibility_cbodies(self):
        '''Loads statements-o-r. from the object into the form.
        '''
        title_string = lambda entity: (
            f'{entity.ordering}. {str(entity.responsibility)}: '
            + f'{str(entity.collectivity)}')
        entity_dict = lambda entity: {
            'entity_id': entity.collectivity.id,
            'responsibility_id': entity.responsibility.id,
            'ordering': entity.ordering
        }
        list_generator = lambda: sorted(
            self.obj.responsibility_collectivities,
            key=lambda item: (item.ordering,
                              item.collectivity.name))

        self.responsibility_collectivities.choices = \
            self.load_stmts_of_responsibility(
                title_string=title_string,
                entity_dict=entity_dict,
                list_generator=list_generator)

    def load_stmts_of_responsibility_individuals(self):
        '''Loads individual document responsibilities from the database
        into the document editing form.
        '''
        title_string = lambda entity: (
            f'{entity.ordering}. {str(entity.responsibility)}: '
            + f'{str(entity.person)}')
        entity_dict = lambda entity: {
            'entity_id': entity.person.id,
            'responsibility_id': entity.responsibility.id,
            'ordering': entity.ordering
        }
        list_generator = lambda: sorted(
            self.obj.responsibilities_people,
            key=lambda item: (item.ordering, item.person.last_name))

        self.responsibilities_people.choices = \
            self.load_stmts_of_responsibility(
                title_string=title_string,
                entity_dict=entity_dict,
                list_generator=list_generator)

    def load_dependent_documents(self):
        description_max_len = 15
        self.dependent_docs.choices = [
            # tuple: option value, text
            (
                # value
                json.dumps({'id': doc.dependent_doc.id,
                            'description': doc.description,
                            'ordering': doc.ordering}),
                # text
                f'{doc.ordering} - '
                + str(doc.dependent_doc)
                + (f' ({doc.description})'[:description_max_len]
                   if doc.description else '')
                + ('...' if len(doc.description) > description_max_len
                   else '')
            )
            for doc in self.obj.dependent_docs]

    def load_items_into_form(self, object_attr=''):
        '''Loads particular attribute of the Document model
        into form.
        '''
        if getattr(self, 'obj'):
            return [(item.id, str(item))
                    for item in getattr(self.obj, object_attr, [])]
        # poniższe do usunięcia
        return []

    def load_languages_as_subjects(self):
        self.language_subjects.choices = self.load_items_into_form(
            'language_subjects')

    def load_publication_places(self):
        self.publication_places.choices = self.load_items_into_form(
            'publication_places')

    def load_collectivity_subjects(self):
        self.collectivity_subjects.choices = self.load_items_into_form(
            'collectivity_subjects')

    def load_keywords(self):
        self.keywords.choices = self.load_items_into_form(
            'keywords')

    def load_topics_people(self):
        self.topic_people.choices = self.load_items_into_form(
            'topic_people')

    def load_subjects_locations(self):
        self.subjects_locations.choices = self.load_items_into_form(
            'subjects_locations')

    @staticmethod
    def save_from_multiselect(form_data, model):
        '''Generic method for saving items from multiple selection fields
        into the database.
        '''
        # przerobić na list compr.
        obj_list = []
        for item_id in form_data:
            item_obj = model.query.get(item_id)
            obj_list.append(item_obj)
        return obj_list

    def save_text_fields(self):
        for field in ['title_proper', 'parallel_title', 'other_title_inf',
                      'edition_statement', 'parallel_edition_stmt',
                      'additional_edition_stmt', 'numbering',
                      'publication_date', 'pagination', 'physical_details',
                      'dimensions', 'accompanying_material', 'series',
                      'note', 'issn', 'isbn_10', 'isbn_13']:
            value = getattr(self, field).data
            setattr(self.obj, field, value)

    def save_document_type(self):
        doc_type = self.document_type.data
        setattr(self.obj, 'document_type', doc_type)

    def save_keywords(self):
        self.obj.keywords = DocumentEditForm.save_from_multiselect(
            self.keywords.raw_data, Keyword)

    def save_subjects_locations(self):
        self.obj.subjects_locations = DocumentEditForm.save_from_multiselect(
            self.subjects_locations.raw_data, GeographicLocation)

    def save_topics_people(self):
        self.obj.topic_people = DocumentEditForm.save_from_multiselect(
            self.topic_people.raw_data, Person)

    def save_publication_places(self):
        self.obj.publication_places = DocumentEditForm.save_from_multiselect(
            self.publication_places.raw_data, GeographicLocation)

    def save_coll_bodies_as_subjects(self):
        self.obj.collectivity_subjects = \
            DocumentEditForm.save_from_multiselect(
            self.collectivity_subjects.raw_data, CollectiveBody)

    def save_languages_as_subjects(self):
        self.obj.language_subjects = DocumentEditForm.save_from_multiselect(
            self.language_subjects.raw_data, Language)

    def save_stmts_of_responsibility(self, form_choices, entity_model,
                                     document_resp):
        choices = []

        for json_data in form_choices.raw_data:
            responsibility_data = json.loads(json_data)
            entity_item = entity_model.query.get(
                responsibility_data['entity_id'])
            responsibility = ResponsibilityName.query.get(
                responsibility_data['responsibility_id'])
            document_responsibility = document_resp(
                entity_item, responsibility)
            document_responsibility.ordering = responsibility_data.get(
                'ordering') or 0
            choices.append(document_responsibility)

        return choices

    def save_dependent_docs(self):
        # czy wpisy z tabeli podłączonej do RelatedDocuments są kasowane?
        self.obj.dependent_docs = []
        new_related_document_pairs = []

        for json_data in self.dependent_docs.raw_data:
            relationship_data = json.loads(json_data)
            dependent_doc_id = relationship_data['id']
            description = relationship_data['description']
            ordering = relationship_data['ordering']

            related_documents = (
                RelatedDocuments.query.filter_by(
                    master_doc_id=self.obj.id,
                    dependent_doc_id=dependent_doc_id).first()
                or
                RelatedDocuments(
                    master_doc=self.obj,
                    dependent_doc=Document.query.get(dependent_doc_id))
            )
            related_documents.ordering = ordering
            related_documents.description = description
            new_related_document_pairs.append(related_documents)

        if new_related_document_pairs:
            db.session.add_all(new_related_document_pairs)

    def save_stmts_of_responsibility_coll_bodies(self):
        def doc_resp_fn(collective_body, responsibility):
            return (
                ResponsibilityCollectivity.query.filter_by(
                    responsibility_id=responsibility.id,
                    collectivity_id=collective_body.id,
                    document_id=self.obj.id).first()

                or ResponsibilityCollectivity(
                    document=self.obj,
                    responsibility=responsibility,
                    collectivity=collective_body))

        self.obj.responsibility_collectivities = \
            self.save_stmts_of_responsibility(
                self.responsibility_collectivities,
                CollectiveBody, document_resp=doc_resp_fn)

    def save_stmts_of_responsibility_individuals(self):
        def doc_resp_fn(person, responsibility):
            # można tą met. tworzyć przy pomocy f. wyższ. rzędu
            return (
                ResponsibilityPerson.query.filter_by(
                    responsibility_id=responsibility.id,
                    person_id=person.id,
                    document_id=self.obj.id).first()

                or ResponsibilityPerson(
                    document=self.obj,
                    responsibility=responsibility,
                    person=person))

        self.obj.responsibilities_people = self.save_stmts_of_responsibility(
            self.responsibilities_people, Person, document_resp=doc_resp_fn)

    @staticmethod
    def save_language(language):
        '''language - self.language or self.original_language reference
        '''
        if language.data:
            return int(language.data)
        else:
            return None

    def save_document_language(self):
        self.obj.language_id = DocumentEditForm.save_language(
            self.language_id)

    def save_original_language(self):
        self.obj.original_language_id = DocumentEditForm.save_language(
            self.original_language_id)

    def redirect_to(self):
        return {'endpoint': 'main.document_view',
                'document_id': self.obj.id}

    id = HiddenField()
    title_proper = StringField(
        'Title proper:',
        render_kw={'required': 'required',
                   'maxlength': f'{length(Document.title_proper)}'})
    parallel_title = StringField(
        'Parallel title:',
        render_kw={'maxlength': f'{length(Document.parallel_title)}'})
    other_title_inf = StringField(
        'Other title information:',
        render_kw={'maxlength': f'{length(Document.other_title_inf)}'})
    edition_statement = StringField(
        'Edition statement:',
        render_kw={'maxlength': f'{length(Document.edition_statement)}'})
    parallel_edition_stmt = StringField(
        'Parallel edition statement',
        render_kw={'maxlength': f'{length(Document.parallel_edition_stmt)}'})
    additional_edition_stmt = StringField(
        'Additional edition statement:',
        render_kw={'maxlength':
                   f'{length(Document.additional_edition_stmt)}'})
    numbering = StringField(
        'Numbering:',
        render_kw={'maxlength': f'{length(Document.numbering)}'})
    publication_date = StringField(
        'Publication date:',
        render_kw={'maxlength': f'{length(Document.publication_date)}'})
    pagination = StringField(
        'Pagination:',
        render_kw={'maxlength': f'{length(Document.pagination)}'})
    physical_details = StringField(
        'Physical details:',
        render_kw={'maxlength': f'{length(Document.physical_details)}'})
    dimensions = StringField(
        'Dimensions:',
        render_kw={'maxlength': f'{length(Document.dimensions)}'})
    accompanying_material = StringField(
        'Accompanying material:',
        render_kw={'maxlength': f'{length(Document.accompanying_material)}'})
    series = StringField(
        'Series:',
        render_kw={'maxlength': f'{length(Document.series)}',
                   'data-toggle': 'tooltip',
                   'title': 'Basic series field'})
    note = TextAreaField(
        'Note:',
        render_kw={'maxlength': f'{length(Document.note)}'})
    issn = StringField(
        'ISSN:',
        render_kw={'maxlength': f'{length(Document.issn)}',
                   'data-toggle': 'tooltip',
                   'title': 'example: 2049-3630',
                   'pattern': '\d{4}-\d{4}'})
    isbn_10 = StringField(
        'ISBN-10:',
        render_kw={'maxlength': f'{length(Document.isbn_10)}',
                   'data-toggle': 'tooltip',
                   'title': 'example: 0-545-01022-5',
                   'pattern': '[\d-]*'})
    isbn_13 = StringField(
        'ISBN-13:',
        render_kw={'maxlength': f'{length(Document.isbn_13)}',
                   'data-toggle': 'tooltip',
                   'title': 'example: 978-3-16-148410-0',
                   'pattern': '[\d-]*'})
    document_type = QuerySelectField(
        'Document type:', query_factory=lambda: DocumentType.query.all(),
        get_label=lambda model: model.name.capitalize(),
        get_pk=lambda model: model.id)
    responsibility_names = QuerySelectField(
        'Select responsibility name:',
        query_factory=lambda: ResponsibilityName.query.all())
    submit = SubmitField(id='submit-document')
    responsibility_collectivities = SelectMultipleField(
        'Statements of responsibility (collective bodies):',
        choices=[])
    responsibilities_people = SelectMultipleField(
        'Statements of responsibility (individuals-people):',
        choices=[])
    language_id = HiddenField()
    original_language_id = HiddenField()
    language = StringField('Document language:',
                           render_kw={'readonly': 'readonly'})
    original_language =  StringField('Original language:',
                           render_kw={'readonly': 'readonly'})
    publication_places = SelectMultipleField(
        'Publication places:', choices=[])
    collectivity_subjects = SelectMultipleField(
        'Collective bodies as document subjects:', choices=[])
    language_subjects = SelectMultipleField(
        'Languages as document subjects:', choices=[])
    keywords = SelectMultipleField(
        'Subject headers (keywords):', choices=[])
    topic_people = SelectMultipleField(
        'Individual (personal) names as topics:', choices=[])
    subjects_locations = SelectMultipleField(
        'Geographic locations as topics:', choices=[])
    dependent_docs = SelectMultipleField(
        'Dependent documents:', choices=[],
        render_kw={'data-toggle': 'tooltip',
                   'title': '''Such as articles within a periodical,
                   parts of the series etc.'''})
    dependent_doc_rel_description = StringField(
        'Relationship description (leave empty if not needed):',
        render_kw={'maxlength': f'{length(RelatedDocuments.description)}'})
