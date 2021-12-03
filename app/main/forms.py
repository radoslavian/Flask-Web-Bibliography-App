from flask_wtf import FlaskForm
from ..models import Language
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length#, Email, Regexp, EqualTo

class LanguageEditForm(FlaskForm):
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
    submit = SubmitField()
