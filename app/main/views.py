'''View functions for the application's main blueprint.
'''

from . import main
from flask import render_template
from flask import request
from app import db
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
                           person_record=person_record)


@main.route('/browse/people/name-variants/id=<variant_id>')
def name_variant(variant_id):
    '''Name variant route for individual (person) name.
    '''
    name_variant = PersonNameVariant.query.filter_by(
        variant_id=variant_id).first_or_404()

    return render_template('person_name_variant.html',
                           name_variant=name_variant)


@main.route('/browse/people/list')
def browse_people():
    '''Displays list of people - individual
    record authorities.
    '''
    page = request.args.get('page', 1, type=int)
    people = Person.query.with_entities(
        Person.person_id,
        Person.forenames,
        Person.last_name,
        Person.life_years,
        db.literal('person'))
    name_variants = PersonNameVariant.query.with_entities(
        PersonNameVariant.variant_id,
        PersonNameVariant.first_name_variant,
        PersonNameVariant.last_name_variant,

        # dummy field, couldn't find any better solution
        db.literal(''),
        db.literal('name_variant'))
    people_variants_union = people.union_all(name_variants).order_by(
        Person.last_name.asc(), Person.forenames.asc())
    pagination = people_variants_union.paginate(
        page, per_page=current_app.config['PEOPLE_POSTS_PER_PAGE'],
        error_out=False)

    return render_template('people_list.html',
                           literal_column=db.literal_column,
                           pagination=pagination)
