from app import db
from sys import stderr
import json
from ..models import *
from flask import flash, request, jsonify
from flask_wtf import FlaskForm
from sqlalchemy.exc import IntegrityError
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms import (StringField, SubmitField, TextAreaField, HiddenField,
                     SelectMultipleField, FieldList)
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length
from app.utils.helpers import length

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

    def commit_row(self):
        try:
            int(self.id.data)
        except ValueError:
            self.id.data = None
            self.row = self.model()
            success_message = 'Successfully created new entry.'
        else:
            # zamiast tego można zapisywać atrybut 'obj' z konstruktora
            self.row = self.model.query.get(self.id.data)
            success_message = 'Entry successfully updated.'
        self.populate_obj(self.row)
        db.session.add(self.row)

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
            flash(success_message)
            return True


class PersonEditForm(ModelEditForm):
    # klasa do poprawienia (czyli refactoringu)
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
        '''Loads variants from object or query into form.
        '''
        if getattr(self, 'obj'):
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
            # może użyć tu yield?
            for variant_id in self.name_variants.raw_data:
                if variant_id.isdigit():
                    variant = PersonNameVariant.query.get(int(variant_id))
                    if variant:
                        variants.append(variant)
            self.row.name_variants = variants
        else:
            self.row.name_variants = []

    def commit_row(self):
        # jak to połączyć z commit_row z nadrzędnej klasy?
        # można zmieniać obie metody (z tej i tamtej klasy)
        # wydzielić elementy wspólne: dodawanie pól tekstowych
        # wg listy tych pól zapisanej w obiekcie
        # elementy różne: relationships
        id_number = self.id.data
        if self.id.data:
            self.row = self.model.query.get(id_number)
            success_message = 'Entry successfully updated.'
        else:
            self.id.data = None
            self.row = self.model()
            success_message = 'Successfully created new entry.'

        # poniższe el. do add_variants() mogą być w metodzie abs.
        # pobranie wartości do pól
        for field in ['forenames', 'last_name', 'note', 'life_years',
                      'birth_date', 'death_date']:
            value = getattr(self, field).data
            setattr(self.row, field, value)

        self.add_variants()
        db.session.add(self.row)

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
            flash(success_message)
            return True

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
                'person_id': self.row.id}


class LanguageEditForm(ModelEditForm):
    def __init__(self, *pargs, **kwargs):
        super().__init__(*pargs, **kwargs)
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
                'language_id': self.row.id}


class DocumentTypeEditForm(ModelEditForm):
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
                'type_id': self.row.id}


class CollectiveBodyEditForm(ModelEditForm):
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
                'c_body_id': self.row.id}


class GeographicLocationEditForm(ModelEditForm):
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
                'location_id': self.row.id}


class KeywordEditForm(ModelEditForm):
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
                'keyword_id': self.row.id}


class ResponsibilityNameEditForm(ModelEditForm):
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
                'responsibility_id': self.row.id}


class PersonNameVariantEditForm(ModelEditForm):
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
                'variant_id': self.row.id}


class DocumentEditForm(ModelEditForm):
    def __init__(self, *pargs, **kwargs):
        super().__init__(*pargs, **kwargs)
        self.model = PersonNameVariant
        if 'obj' in kwargs:
            self.header = 'Update Document entry:'
        else:
            self.header = 'Create new Document entry:'

        self.load_stmts_of_responsibility_cbodies()
        self.load_stmts_of_responsibility_individuals()

    def validate_on_submit(self):
        if request.method == 'POST':
            return True
        else:
            return False

    def commit_row(self):
        self.save_stmts_of_responsibility_coll_bodies()
        self.save_stmts_of_responsibility_individuals()
        self.save_document_language()
        self.save_original_language()
        self._commit()

    def _commit(self):
        # przenieść do głównej klasy
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
            flash('Successfully updated document')
            return True

    def load_stmts_of_responsibility(self, title_string, entity_dict,
                                    list_generator):
        '''General method for loading statements of responsibility.
        '''
        if getattr(self, 'obj'):
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
            self.load_stmts_of_responsibility(title_string=title_string,
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
            self.load_stmts_of_responsibility(title_string=title_string,
                                              entity_dict=entity_dict,
                                              list_generator=list_generator)

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
                'document_id': self.row.id}

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
                   'pattern': '\d-\d{4}-\d{4}-\d'})
    isbn_13 = StringField(
        'ISBN-13:',
        render_kw={'maxlength': f'{length(Document.isbn_13)}',
                   'data-toggle': 'tooltip',
                   'title': 'example: 978-3-16-148410-0',
                   'pattern': '\d{3}-\d-\d{2}-\d{6}-\d'})
    document_type = QuerySelectField(
        'Document type:', query_factory=lambda: DocumentType.query.all(),
        get_label=lambda model: model.name.capitalize())
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
