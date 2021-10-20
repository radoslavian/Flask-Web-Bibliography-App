'''View functions for the the application main blueprint.
'''

from . import main
from flask import render_template, request, current_app
from app import db
from ..models import *

@main.route('/browse/people/')
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
        page, per_page=current_app.config['LIST_ENTRIES_PER_PAGE'],
        error_out=False)

    return render_template('people_list.html',
                           literal_column=db.literal_column,
                           pagination=pagination)


@main.route('/browse/documents/id=<document_id>', methods=['GET', 'POST'])
def document_view(document_id):
    document = Document.query.filter_by(
        document_id=document_id).first_or_404()

    return render_template('document.html', document=document)


@main.route('/browse/documents/')
def browse_documents():
    pass


@main.route('/browse/geographic-locations/id=<location_id>')
def geographic_location_details(location_id):
    location = GeographicLocation.query.filter_by(
        location_id=location_id).first_or_404()

    return render_template('geographic_location_details.html',
                           location=location)


@main.route('/browse/geographic-locations/')
def geographic_locations_list():
    page = request.args.get('page', 1, type=int)
    locations = GeographicLocation.query.order_by(GeographicLocation.name)
    pagination = locations.paginate(
        page, per_page=current_app.config['LIST_ENTRIES_PER_PAGE'],
        error_out=False)

    return render_template('geographic_locations_list.html',
                           pagination=pagination)


@main.route('/', methods=['GET', 'POST'])
def index():
    # url_for('main.index') # main - przestrzeń nazw
    # url_for('.index') # przestrzeń n. akt. żądania

    return render_template('index.html')


@main.route('/browse/keywords/id=<keyword_id>')
def keyword_details(keyword_id):
    keyword = Keyword.query.filter_by(id=keyword_id).first_or_404()

    return render_template('keyword_details_view.html',
                           keyword=keyword)


@main.route('/browse/keywords/')
def keywords_list():
    page = request.args.get('page', 1, type=int)
    keywords = Keyword.query.order_by(Keyword.keyword)
    pagination = keywords.paginate(
        page, per_page=current_app.config['LIST_ENTRIES_PER_PAGE'],
        error_out=False)

    return render_template('keywords_list.html',
                           pagination=pagination)


@main.route('/browse/people/name-variants/id=<variant_id>')
def name_variant(variant_id):
    '''Name variant route for individual (person) name.
    '''
    name_variant = PersonNameVariant.query.filter_by(
        variant_id=variant_id).first_or_404()

    return render_template('person_name_variant.html',
                           name_variant=name_variant)


def get_responsibilities(record):
    '''Returns unique list (set) of responsibilities for person
    and CollectiveBody models.
    '''
    return {item.responsibility.responsibility_name
            for item in record.responsibilities}


def person_responsibility_list(responsibilities, person_id):
    '''List of responsibilities and-for each one-count of documents
    in which a given person appears with a particular responsibility.
    '''
    responsibilities_list = []
    for responsibility_name in responsibilities:
        resp_id = ResponsibilityName.query.filter_by(
            responsibility_name=responsibility_name).first().id
        resp_count = ResponsibilityPerson.query.filter_by(
            person_id=person_id, responsibility_id=resp_id).count()
        responsibilities_list.append(
            [responsibility_name, resp_count])
    responsibilities_list.sort(key=lambda item: item[0])

    return responsibilities_list


def collective_body_resp_list(responsibilities, c_body_id):
    '''List of responsibilities and-for each one-count of documents
    in which a given collective body appears with a particular responsibility.
    '''
    responsibilities_list = []
    for responsibility_name in responsibilities:
        resp_id = ResponsibilityName.query.filter_by(
            responsibility_name=responsibility_name).first().id
        resp_count = ResponsibilityCollectivity.query.filter_by(
            collectivity_id=c_body_id, responsibility_id=resp_id).count()
        responsibilities_list.append(
            [responsibility_name, resp_count])
    responsibilities_list.sort(key=lambda item: item[0])

    return responsibilities_list


@main.route('/browse/people/id=<person_id>')
def person_details(person_id):
    '''Route for detailed view of person authority (people as
    document's authors, translators, subjects etc.)
    '''
    person_record = Person.query.filter_by(person_id=person_id).first_or_404()
    responsibilities = get_responsibilities(person_record)
    person_record.responsibilities_list = person_responsibility_list(
        responsibilities, person_id)

    return render_template('person_record_details.html',
                           person_record=person_record)


@main.route('/browse/collective-bodies/id=<c_body_id>')
def collective_body_details(c_body_id):
    '''Route for detailed view of collective body record.
    '''
    collective_body_record = CollectiveBody.query.filter_by(
        id=c_body_id).first_or_404()
    responsibilities = get_responsibilities(collective_body_record)
    collective_body_record.responsibilities_list = collective_body_resp_list(
        responsibilities, c_body_id)

    return render_template('collective_body_details.html',
                           collective_body=collective_body_record)


@main.route('/browse/collective-bodies/')
def collective_bodies_list():
    page = request.args.get('page', 1, type=int)
    collective_bodies = CollectiveBody.query.order_by(
        CollectiveBody.name)
    pagination = collective_bodies.paginate(
        page, per_page=current_app.config['LIST_ENTRIES_PER_PAGE'],
        error_out=False)

    return render_template('collective_bodies_list.html',
                           pagination=pagination)


@main.route('/search')
def search():
    '''Route for full-text search.
    '''
    return request.args.get('to be written')
