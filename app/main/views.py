'''View functions for the the application main blueprint.
'''

from . import main
from flask import render_template, request, current_app
from app import db
from ..models import *

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
        page, per_page=current_app.config['PEOPLE_ENTRIES_PER_PAGE'],
        error_out=False)

    return render_template('people_list.html',
                           literal_column=db.literal_column,
                           pagination=pagination)


@main.route('/browse/documents/id=<document_id>', methods=['GET', 'POST'])
def document_view(document_id):
    document = Document.query.filter_by(
        document_id=document_id).first_or_404()

    return render_template('document.html', document=document)


@main.route('/browse/documents/list')
def browse_documents():
    pass


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


@main.route('/browse/keywords/list')
def keywords_list():
    page = request.args.get('page', 1, type=int)
    keywords = Keyword.query.order_by(Keyword.keyword)
    pagination = keywords.paginate(
        page, per_page=current_app.config['KEYWORD_ENTRIES_PER_PAGE'],
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


@main.route('/browse/people/id=<person_id>')
def person_details(person_id):
    '''Route for detailed view of person authority (people as
    document's authors, translators, subjects etc.)
    '''
    person_record = Person.query.filter_by(person_id=person_id).first_or_404()
    responsibilities = {person_resp.responsibility.responsibility_name
                        for person_resp in
                        person_record.responsibilities}

    person_record.responsibilities_list = []
    for responsibility_name in responsibilities:
        resp_id = ResponsibilityName.query.filter_by(
            responsibility_name=responsibility_name).first().id
        resp_count = ResponsibilityPerson.query.filter_by(
            person_id=person_id, responsibility_id=resp_id).count()
        person_record.responsibilities_list.append(
            [responsibility_name, resp_count])
    person_record.responsibilities_list.sort(key=lambda item: item[0])

    return render_template('person_record_details.html',
                           person_record=person_record)


@main.route('/search')
def search():
    '''Route for full-text search.
    '''
    return request.args.get('q') # dummy response
