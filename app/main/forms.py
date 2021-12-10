from app import db
from sys import stderr
from ..models import *
from flask import g, flash, request
from flask_wtf import FlaskForm
from sqlalchemy.exc import IntegrityError
from wtforms import (StringField, SubmitField, TextAreaField, HiddenField,
                     SelectMultipleField)
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
            self.submit.label.text = 'Update entity'
        else:
            self.submit.label.text = 'Create new'
        self.header = 'Edit Form Header'

    def redirect_to(self):
        '''Returns arguments for the url_for().
        '''
        pass

    def commit_row(self):
        id_number = self.id.data
        if id_number.isdigit():
            # zamiast tego można zapisywać atrybut 'obj' z konstruktora
            self.row = self.model.query.get(id_number)
            success_message = 'Entry successfully updated.'
        else:
            self.id.data = None
            self.row = self.model()
            success_message = 'Successfully created new entry.'
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


class PersonEditForm(ModelEditForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.obj = kwargs.get('obj', None)
        self.model = Person
        if self.id.data:
            self.header = 'Update Person entry:'
        else:
            self.header = 'Create new Person entry:'
        self.get_variants()

    def validate_on_submit(self):
        if request.method == 'POST':
            return True
        else:
            return False

    def get_variants(self):
        if getattr(self, 'obj'):
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
        if not self.name_variants.raw_data:
            return
        variants = []
        # takie samo jak w get_variants
        # może użyć tu yield?
        for variant_id in self.name_variants.raw_data:
            if variant_id.isdigit():
                variant = PersonNameVariant.query.get(int(variant_id))
                if variant:
                    variants.append(variant)
        self.row.name_variants = variants

    def commit_row(self):
        # jak to połączyć z commit_row z nadrzędnej klasy?
        # można zmieniać obie metody (z tej i tamtej klasy)
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
    forenames = StringField('Forenames (first/second name):')
    last_name = StringField('Last name:')
    note = TextAreaField('Note:')
    life_years = StringField('Life years (text format):')
    birth_date = DateField('Exact birth date:')
    death_date = DateField('Exact expiration date:')
    name_variants = SelectMultipleField('Name Variants:', choices=[])
    submit = SubmitField(id='submit_form')

    def redirect_to(self):
        return {'endpoint': 'main.person_details',
                'person_id': self.row.id}
