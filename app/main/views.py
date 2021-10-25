'''View functions for the the application main blueprint.
'''

__name__ = 'views'

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
    responsibility_id = request.args.get(
        'responsibility_id', None, type=int)
    responsibility = None
    if responsibility_id:

        # ta kwerenda działa, ale funkcja/logika
        # do wyświetlania tej listy wymagają
        # zmiany (druga funkcja dla innej trasy
        # lub inne rozwiązanie)
        # lepsza kwerenda:
        # Flask Web..., s. 182
        # sprawdzić czy działa:
        # db.session.query(Person).select_from(ResponsibilityPerson) \
        # .filter(ResponsibilityPerson.responsibility_id==1) \
        # .join(Person, ResponsibilityPerson.person_id == Person.person_id) \
        # .all()
        # (na kolejnych stronach przepis na prostszą wersję)

        responsibility = ResponsibilityName.query.filter_by(
            id=responsibility_id).first_or_404()
        result = ResponsibilityPerson.query.join(
            ResponsibilityPerson.responsibility).filter_by(
                id=responsibility_id).join(
                    ResponsibilityPerson.person).with_entities(
                        Person.person_id,
                        Person.forenames,
                        Person.last_name,
                        Person.life_years,
                        db.literal('person')
                    )
    else:
        people = ResponsibilityPerson.query.with_entities(
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
        result = people.union_all(name_variants).order_by(
            Person.last_name.asc(), Person.forenames.asc())
    pagination = result.paginate(
        page, per_page=current_app.config['LIST_ENTRIES_PER_PAGE'],
        error_out=False)

    responsibility_name = None
    if responsibility:
        responsibility_name = responsibility.responsibility_name

    return render_template(
        'people_list.html',
        responsibility_name=responsibility_name,
        responsibility_id=responsibility_id,
        literal_column=db.literal_column,
        endpoint='.browse_people',
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

    return render_template(
        'geographic_locations_list.html',
        title='List of geographic locations',
        subtitle='Ordered alphabetically, ascending.',
        pagination=pagination,
        endpoint='.geographic_locations_list')


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
                           title='List of subject headers from the database',
                           subtitle='Ordered alphabetically, ascending.',
                           pagination=pagination,
                           endpoint='.keywords_list')


@main.route('/browse/languages/')
def language_list():
    page = request.args.get('page', 1, type=int)
    languages = Language.query.order_by(Language.language_name)
    pagination = languages.paginate(
        page, per_page=current_app.config['LIST_ENTRIES_PER_PAGE'],
        error_out=False)

    return render_template(
        'list_of_items.html',
        title='List of languages in the database',
        subtitle='Alphabetical order, ascending',
        pagination=pagination,
        endpoint='.language_list',
        partial_template_name='_language_list.html')


@main.route('/browse/languages/id=<language_id>')
def language_details(language_id):
    language = Language.query.filter_by(
        language_id=language_id).first_or_404()

    return render_template('language_details.html',
                           language=language)


@main.route('/browse/people/name-variants/id=<variant_id>')
def name_variant(variant_id):
    '''Name variant route for individual (person) name.
    '''
    name_variant = PersonNameVariant.query.filter_by(
        variant_id=variant_id).first_or_404()

    return render_template('person_name_variant.html',
                           name_variant=name_variant)


def get_unique_responsibilities(item_responsibilities):
    '''Returns unique list (set) of responsibilities
    from a responsibility relationship in a model.
    '''
    return {responsibility_person.responsibility
            for responsibility_person in item_responsibilities}


def responsibility_list(responsibilities, query_fn):
    '''Lists responsibilities from a collective body or person relationship
    field and counts number of documents for each one
    in which a given entity appears with a particular responsibility.
    '''

    responsibilities_list = []
    for responsibility in responsibilities:
        resp_count = query_fn(responsibility).count()
        responsibilities_list.append(
            [responsibility, resp_count])
    responsibilities_list.sort(key=lambda item: item[0].responsibility_name)

    return responsibilities_list


@main.route('/browse/people/id=<person_id>')
def person_details(person_id):
    '''Route for detailed view of person authority (people as
    document's authors, translators, subjects etc.)
    '''
    person_record = Person.query.filter_by(person_id=person_id).first_or_404()
    responsibilities = get_unique_responsibilities(
        person_record.responsibilities)
    person_record.responsibilities_list = responsibility_list(
        responsibilities,
        query_fn=lambda responsibility: ResponsibilityPerson.query.filter_by(
            person_id=person_id,
            responsibility_id=responsibility.id))

    return render_template('person_record_details.html',
                           person_record=person_record)


@main.route('/browse/responsibilities/')
def responsibilities_list():
    responsibilities = ResponsibilityName.query.order_by(
        ResponsibilityName.responsibility_name).all()

    return render_template(
        'list_of_items.html',
        responsibilities=responsibilities,
        title='List of document responsibilities',
        subtitle='Alphabetical order, ascending',
        partial_template_name='_responsibilities.html')


@main.route('/browse/responsibilities/id=<responsibility_id>')
def responsibility_details(responsibility_id):
    responsibility = ResponsibilityName.query.filter_by(
        id=responsibility_id).first_or_404()

    return render_template('responsibility_details.html',
                           responsibility=responsibility)


@main.route('/browse/collective-bodies/id=<c_body_id>')
def collective_body_details(c_body_id):
    '''Route for detailed view of collective body record.
    '''
    collective_body_record = CollectiveBody.query.filter_by(
        id=c_body_id).first_or_404()
    responsibilities = get_unique_responsibilities(
        collective_body_record.responsibilities)
    collective_body_record.responsibilities_list = responsibility_list(
        responsibilities,
        query_fn=lambda responsibility: ResponsibilityCollectivity. \
        query.filter_by(collectivity_id=c_body_id,
                        responsibility_id=responsibility.id))

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

    return render_template(
        'list_of_items.html',
        title='List of collective bodies from the database',
        subtitle='Alphabetical order, ascending',
        endpoint='.collective_bodies_list',
        pagination=pagination,
        partial_template_name='_collective_bodies_list.html')


@main.route('/browse/document-types/id=<type_id>')
def document_type(type_id):
    '''Route for details of the document type entry from
    the database, identified by type_id.
    '''
    document_type = DocumentType.query.filter_by(
        type_id=type_id).first_or_404()

    return render_template('document_type_details.html',
                           document_type=document_type)


@main.route('/browse/document-types/')
def document_types_list():
    '''Generates view for the list of document types from the database.
    '''
    document_types = DocumentType.query.order_by(
        DocumentType.name).all()

    return render_template('list_of_items.html',
                           pagination=None,
                           title='List of document types',
                           partial_template_name='_document_types_list.html',
                           subtitle='Alphabetical order, ascending',
                           document_types=document_types)

# @main.route('/browse/documents/')
# def documents_list(query_fn=None):
#     def default_query_fn():
#         pass
#     pass


@main.route('/search')
def search():
    '''Route for full-text search.
    '''
    return 'to be written'
