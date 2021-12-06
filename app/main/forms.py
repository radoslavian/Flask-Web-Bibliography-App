from app import db
from sys import stderr
from ..models import *
from flask import flash
from flask_wtf import FlaskForm
from sqlalchemy.exc import IntegrityError
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

def length(model_col):
    '''Get length of the database column string field.
    '''
    return model_col.property.columns[0].type.length


class ModelEditForm(FlaskForm):
    '''Abstract class for entity editing forms.
    Form fields should have the same names as attributes 
    in the database model.

    Following attributes in inheriting classes are expected:
    self.fields - list of database/form fields
    self.model - reference to the database model
    '''
    submit = SubmitField()

    def __init__(self):
        FlaskForm.__init__(self)
        self.row = None
        self.submit.label.text = 'Create new'

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
            flash(f'Failed to perform operation due to '
                  'the data integrity error.')
            print(f'Failed to perform operation: {err}', file=stderr)
            return False
        else:
            return True


class LanguageEditForm(ModelEditForm):
    def __init__(self):
        ModelEditForm.__init__(self)
        self.fields = ['language_name', 'native_name', 'other_name',
                       'iso_639_1_language_code', 'iso_639_2_language_code']
        self.model = Language

    language_name = StringField('Language name:', validators=[
        DataRequired(),
        Length(1, Language.language_name.property.columns[0].type.length)])
    native_name = StringField('Native language name:', validators=[
        Length(max=Language.native_name.property.columns[0].type.length)])
    other_name = StringField('Other name:', validators=[
        Length(max=Language.other_name.property.columns[0].type.length)])
    iso_639_1_language_code = StringField(
        'ISO-639-1 language code:', validators=[Length(max=2)])
    iso_639_2_language_code = StringField(
        'ISO-639-2 language code:', validators=[Length(max=3)])

    def redirect_to(self):
        return {'endpoint': 'main.language_details',
                'language_id': self.row.id}


class DocumentTypeEditForm(ModelEditForm):
    def __init__(self):
        ModelEditForm.__init__(self)
        self.fields = ['name', 'description']
        self.model = DocumentType

    name = StringField(
        'Document type name:', validators=[
            DataRequired(),
            Length(max=DocumentType.name.property.columns[0].type.length)])
    description = TextAreaField('Description:', validators=[
        Length(max=DocumentType.description.property.columns[0].type.length)])

    def redirect_to(self):
        return {'endpoint': '.document_type',
                'type_id': self.row.id}


class CollectiveBodyEditForm(ModelEditForm):
    def __init__(self):
        ModelEditForm.__init__(self)
        self.fields = ['name', 'address', 'abbr', 'description']
        self.model = CollectiveBody

    name = StringField(
        'Collective body name:', validators=[
            DataRequired(),
            Length(max=CollectiveBody.name.property.columns[0].type.length)])
    address = StringField(
        'Address:', validators=[
            Length(max=CollectiveBody.address\
                   .property.columns[0].type.length)])
    abbr = StringField(
        'Formal abbreviation:',
        validators=[Length(max=CollectiveBody\
                           .abbr.property.columns[0].type.length)])
    description = TextAreaField(
        'Description:',
        validators=[Length(max=CollectiveBody\
                           .description.property.columns[0].type.length)])

    def redirect_to(self):
        return {'endpoint': 'main.collective_body_details',
                'c_body_id': self.row.id}


class GeographicLocationEditForm(ModelEditForm):
    def __init__(self):
        ModelEditForm.__init__(self)
        self.fields = ['name', 'native_name', 'other_name', 'determiner',
                       'note']
        self.model = GeographicLocation

    name = StringField(
        'Name:', validators=[
            DataRequired(),
            Length(max=GeographicLocation.name\
                   .property.columns[0].type.length)])
    native_name = StringField(
        'Native name:', validators=[
            Length(max=GeographicLocation.native_name\
                   .property.columns[0].type.length)])
    other_name = StringField(
        'Other name:', validators=[
            Length(max=GeographicLocation.other_name\
                   .property.columns[0].type.length)])
    determiner = StringField(
        'Determiner:', validators=[
            Length(max=GeographicLocation.determiner\
                   .property.columns[0].type.length)])
    note = TextAreaField(
        'Note:', validators=[
            Length(max=GeographicLocation.note\
                   .property.columns[0].type.length)])

    def redirect_to(self):
        return {'endpoint': 'main.geographic_location_details',
                'location_id': self.row.id}


class KeywordEditForm(ModelEditForm):
    def __init__(self):
        ModelEditForm.__init__(self)
        self.fields = ['keyword', 'determiner']
        self.model = Keyword

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
    pass
