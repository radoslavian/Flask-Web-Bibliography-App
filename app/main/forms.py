from app import db
from sys import stderr
from ..models import *
from flask import flash
from flask_wtf import FlaskForm
from sqlalchemy.exc import IntegrityError
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from app.utils.helpers import length

class ModelEditForm(FlaskForm):
    '''Abstract class for entity editing forms.
    Form fields should have the same names as attributes 
    in the database model.

    Following instance attributes in inheriting classes are
    expected:
    self.fields - list of database/form fields
    self.model - reference to the database model
    '''
    submit = SubmitField()

    def __init__(self):
        FlaskForm.__init__(self)
        self.row = None
        self.submit.label.text = 'Create new'
        self.header = 'Edit Form Header'

    def load_row(self, id_number):
        primary_key = getattr(self.model, '__primary_key__')
        self.row = self.model.query.filter(
            getattr(self.model, primary_key) == id_number
        ).first_or_404()

    def fill_form(self):
        '''Fill the form with data from the database row.
        '''
        for field_name in self.fields:
            field = getattr(self, field_name)
            if not field.data:
                field.data = getattr(self.row, field_name)
        self.submit.label.text = 'Save changes'

    def data_from_form(self):
        for field_name in self.fields:
            field_value = getattr(self, field_name).data
            setattr(self.row, field_name, field_value)

    def redirect_to(self):
        '''Returns arguments for the url_for().
        '''
        pass

    def commit_row(self):
        if not self.row:
            self.row = self.model()
        self.data_from_form()
        db.session.add(self.row)

        try:
            db.session.commit()
        except IntegrityError as err:
            db.session.rollback()
            flash('Failed to perform operation due to '
                  'the data integrity error.')
            print(f'Failed to perform operation: {err}', file=stderr)
            return False
        else:
            return True


class LanguageEditForm(ModelEditForm):
    def __init__(self):
        super().__init__()
        self.fields = ['language_name', 'native_name', 'other_name',
                       'iso_639_1_language_code', 'iso_639_2_language_code']
        self.model = Language
        self.header = 'Create new Language entry:'

    def fill_form(self):
        super().fill_form()
        self.header = f'Edit Language entry (id {self.row.id}):'

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
    def __init__(self):
        super().__init__()
        self.fields = ['name', 'description']
        self.model = DocumentType
        self.header = 'Add new Document Type entry:'

    def fill_form(self):
        super().fill_form()
        self.header = f'Edit Document Type entry (id {self.row.id}):'

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
    def __init__(self):
        super().__init__()
        self.fields = ['name', 'address', 'abbr', 'description']
        self.model = CollectiveBody
        self.header = 'Add new Collective Body entry:'

    def fill_form(self):
        super().fill_form()
        self.header = f'Edit Collective Body entry (id {self.row.id}):'

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
    def __init__(self):
        super().__init__()
        self.fields = ['name', 'native_name', 'other_name', 'determiner',
                       'note']
        self.model = GeographicLocation
        self.header = 'Create new Geographic Location entry:'

    def fill_form(self):
        super().fill_form()
        self.header = f'Edit Geographic Location entry (id {self.row.id}):'

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
    def __init__(self):
        super().__init__()
        self.fields = ['keyword', 'determiner']
        self.model = Keyword
        self.header = 'Create new Keyword (subject header) entry:'

    def fill_form(self):
        super().fill_form()
        self.header = f'Edit Keyword (subject header) '\
        f'entry (id {self.row.id}):'

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
    def __init__(self):
        super().__init__()
        self.fields = ['responsibility_name', 'responsibility_abbr']
        self.model = ResponsibilityName
        self.header = 'Create new Responsibility Name entry:'

    def fill_form(self):
        super().fill_form()
        self.header = f'Edit Responsibility Name entry (id {self.row.id}):'

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
    def __init__(self):
        super().__init__()
        self.fields = ['first_name_variant', 'last_name_variant',
                       'variant_notes']
        self.model = PersonNameVariant
        self.header = 'Create new person name variant entry:'

    def fill_form(self):
        super().fill_form()
        self.header = f'Edit person name variant entry (id {self.row.id}):'

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
