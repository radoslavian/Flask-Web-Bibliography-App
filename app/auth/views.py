'''View functions for the authorization blueprint.
Mostly adapted from: M. Grinberg...
'''

from flask import render_template, url_for, flash, request, redirect
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import db, User
from .forms import *

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember_me.data)
            next_page = request.args.get('next')
            if next_page is None or not next.startswith('/'):
                next_page = url_for('main.index')
            return redirect(next_page)
        flash('Invalid username or password.')
    return render_template('auth/login.html', login_form=login_form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Now you can log in.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', registration_form=form)
