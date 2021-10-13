'''View functions for the application main blueprint.
'''

from . import main
from flask import render_template, url_for
from flask import request
from ..models import *

@main.route('/', methods=['GET', 'POST'])
def index():
    # url_for('main.index') # main - przestrzeń nazw
    # url_for('.index') # przestrzeń n. akt. żądania

    return render_template('index.html')


@main.route('/search')
def search():
    '''Route for full-text search.
    '''
    return request.args.get('q') # dummy response


@main.route('/browse/people/id=<person_id>')
def person_details(person_id):
    '''Route for detailed view of person authority (people as
    document's authors, translators, subjects etc.)
    '''
    person_record = Person.query.filter_by(person_id=person_id).first_or_404()

    return render_template('person_record_details.html',
                           person_record=person_record,
                           url_for=url_for)


@main.route('/browse/people/name-variants/id=<variant_id>')
def name_variant(variant_id):
    '''Name variant route for individual (person) name.
    '''
    name_variant = PersonNameVariant.query.filter_by(
        variant_id=variant_id).first_or_404()

    return render_template('person_name_variant.html',
                           name_variant=name_variant,
                           url_for=url_for)
