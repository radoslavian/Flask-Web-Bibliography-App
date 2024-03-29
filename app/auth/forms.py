from flask_wtf import FlaskForm
from ..models import User
from wtforms import (StringField, PasswordField, BooleanField, SubmitField,
                     ValidationError)
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    '''Adapted from M. Grinberg...
    '''
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField(
        'Username', validators=[
            DataRequired(), Length(1, 64),
            # ^[\w\d_.]$ - tak nie lepiej?
            Regexp('^[A-Za-z][A-Z-a-z0-9_.]*$', 0,
                   'Usernames must have only letters numbers, dots '
                   'or underscores')])
    password = PasswordField(
        'Password',
        validators=[DataRequired(), EqualTo('password2',
                                            message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use')
