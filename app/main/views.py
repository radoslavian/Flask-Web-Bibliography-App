'''View functions for the the application main blueprint.
'''

__name__ = 'views'

from . import main
from flask import abort, render_template, session, redirect, url_for
from app import db
from app import queries
from ..models import *
from app.helpers import *

@main.route('/browse/people/')
def browse_people():
    '''Displays list of people - individual record authorities.
    '''
    responsibility_id, responsibility_name = get_responsibility_identifiers(
        request.args.get('responsibility_id', None, type=int))

    if responsibility_id is not None:
        query = db.session.query(Person).select_from(
            ResponsibilityPerson).filter(
                ResponsibilityPerson \
                .responsibility_id == responsibility_id).join(
                    Person,
                    ResponsibilityPerson.person_id == Person.person_id)
    else:
        query = queries.list_people_name_variants()

    return render_template(
        'people_list.html',
        subtitle=(f'Responsibility: {responsibility_name.capitalize()}' if
                  responsibility_name else 'Alphabetical order, ascending.'),
        responsibility_id=responsibility_id,
        literal_column=db.literal_column,
        endpoint='.browse_people',
        pagination=paginate(query))


@main.route('/browse/documents/id=<document_id>', methods=['GET', 'POST'])
def document_view(document_id):
    document = Document.query.filter_by(
        document_id=document_id).first_or_404()

    return render_template('document.html', document=document)


@main.route('/browse/geographic-locations/id=<location_id>')
def geographic_location_details(location_id):
    location = GeographicLocation.query.filter_by(
        location_id=location_id).first_or_404()

    return render_template('geographic_location_details.html',
                           location=location)


@main.route('/browse/geographic-locations/')
def geographic_locations_list():
    locations = GeographicLocation.query.order_by(GeographicLocation.name)
    
    return render_template(
        'geographic_locations_list.html',
        title='List of geographic locations',
        subtitle='Ordered alphabetically, ascending.',
        pagination=paginate(locations),
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
    keywords = Keyword.query.order_by(Keyword.keyword)

    return render_template('keywords_list.html',
                           title='List of subject headers from the database',
                           subtitle='Ordered alphabetically, ascending.',
                           pagination=paginate(keywords),
                           endpoint='.keywords_list')


@main.route('/browse/languages/')
def language_list():
    languages = Language.query.order_by(Language.language_name)

    return render_template(
        'list_of_items.html',
        title='List of languages in the database',
        subtitle='Alphabetical order, ascending',
        pagination=paginate(languages),
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
    responsibility_id, responsibility_name = get_responsibility_identifiers(
        request.args.get('responsibility_id', None, type=int))

    if responsibility_id is not None:
        query = db.session.query(CollectiveBody).select_from(
            ResponsibilityCollectivity).filter(
                ResponsibilityCollectivity \
                .responsibility_id == responsibility_id).join(
                    CollectiveBody,
                    ResponsibilityCollectivity \
                    .collectivity_id == CollectiveBody.id)
    else:
        query = CollectiveBody.query.order_by(
            CollectiveBody.name)

    return render_template(
        'collective_bodies_list.html',
        subtitle=(f'Responsibility: {responsibility_name.capitalize()}' if
                  responsibility_name else 'Alphabetical order, ascending.'),
        responsibility_id=responsibility_id,
        endpoint='.collective_bodies_list',
        pagination=paginate(query))


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


from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField

def get_type_ids(document_types_form):
    '''Returns dictionary of DocumentType ids with values (True/False)
    from document_list.SelectDocumentTypes form.
    '''
    selected_doc_types_ids = []
    for fieldname, value in document_types_form.data.items():
        field_id = str(getattr(document_types_form, fieldname).id)
        if field_id.isnumeric() and value:
            selected_doc_types_ids.append(int(field_id))
    return selected_doc_types_ids


@main.route('/browse/documents/', methods=['GET', 'POST'])
def documents_list():
    class SelectDocumentTypes(FlaskForm):
        for doc in DocumentType.query.order_by(
                DocumentType.name).all():
            # ten fragment może doprowadzić do nieprzewidzianego
            # zachowania
            selected_doc_types_ids =  session.get('selected_doc_types_ids')
            locals()[f'doctype_{doc.type_id}'] = BooleanField(
                doc.name.capitalize(), id=doc.type_id,
                default='checked' if doc.type_id in
                selected_doc_types_ids else '')
        submit = SubmitField('Apply filter')

    start_page = 0
    document_types_form = SelectDocumentTypes()
    session['selected_doc_types_ids'] = get_type_ids(document_types_form)
    if session.get(
            'prev_selected_doc_types_ids') != session.get(
                'selected_doc_types_ids'):
        start_page = 1
        session['prev_selected_doc_types_ids'] = session.get(
            'selected_doc_types_ids')

    search_parameters = {}
    # source entry for document list (collective body, person etc.)
    search_parameters['by_entry_type'] = request.args.get(
        'by_entry_type', None)
    search_parameters['filter_type'] = request.args.get(
        'filter_type', None)
    search_parameters['id_number'] = request.args.get(
        'id_number', None, type=int)
    (search_parameters['responsibility_id'],
     responsibility_name) = get_responsibility_identifiers(request.args.get(
         'responsibility_id', None, type=int))
    subtitle = None

    if search_parameters['by_entry_type'] == 'collective_body':
        # collective-body search

        collective_body = CollectiveBody.query.filter_by(
            id=search_parameters['id_number']).first_or_404()
        if search_parameters['filter_type'] == 'by_subject':
            # collective body as a subject

            query = collective_body.documents_topics
            subtitle = f'''Documents where collective body
            <em>{collective_body.name}</em> is a subject.'''
        elif search_parameters['filter_type'] == 'by_responsibility':
            # collective body as a responsibility

            # czy tą kwerendę da się poprawić?
            query = db.session.query(Document).select_from(
                ResponsibilityCollectivity).filter(
                    ResponsibilityCollectivity \
                    .responsibility_id == search_parameters[
                        'responsibility_id']
                ).join(Document,
                       ResponsibilityCollectivity \
                       .document_id == Document.document_id).filter(
                           ResponsibilityCollectivity.collectivity_id \
                           == search_parameters['id_number'])
            subtitle = f'''Documents where collective body
            <em>{collective_body.name}</em> holds responsibility -
            <em>{responsibility_name}</em>:'''
        else:
            # w razie błędnego URL zawsze powinno wyświetlać 404
            abort(404)
    elif search_parameters['by_entry_type'] == 'person':
        person = Person.query.filter_by(
            person_id=search_parameters['id_number']).first_or_404()

        if search_parameters['filter_type'] == 'by_subject':
            # person as a subject list
            query = person.documents_topics
            subtitle = f'''Documents where an individual name
            <em>{person.forenames} {person.last_name}</em> is a subject.'''

        elif search_parameters['filter_type'] == 'by_responsibility':
            query = db.session.query(Document).select_from(
                ResponsibilityPerson).filter(
                    ResponsibilityPerson \
                    .responsibility_id == search_parameters[
                        'responsibility_id']
                ).join(Document,
                       ResponsibilityPerson \
                       .document_id == Document.document_id).filter(
                           ResponsibilityPerson.person_id \
                           == search_parameters['id_number'])
            subtitle = f'''Documents where <em>{person.forenames}
            {person.last_name}</em> holds responsibility:
            <em>{responsibility_name}</em>.'''
    else:
        # jeżeli nie ma entry_type, zawsze będzie tu wpadać
        # a powinno być abort()
        # z czego wniosek - wzorzec dopasowania trzeba będzie rozpisać
        # na diagramie i poprawić

        # at this point, search parameters should be reset to None
        # otherwise, if keys exist, they would appear in a page
        # URL
        search_parameters = {}
        query = Document.query

    if len(session.get(
            'selected_doc_types_ids')) != DocumentType.query.count():
        query = query.filter(Document.document_type_id.in_(
            session.get('selected_doc_types_ids')))
    query = query.order_by(Document.title_proper)
    kargs = search_parameters

    if request.method == 'POST':
        return redirect(url_for('.documents_list', **kargs))

    return render_template(
        'list_of_items.html',
        kargs=kargs,
        subtitle=subtitle,
        pagination=paginate(query, start_page=start_page),
        document_types=document_types_form,
        title='List of the document titles from the database',
        partial_template_name='_documents_list.html',
        endpoint='.documents_list')


@main.route('/search')
def search():
    '''Route for full-text search.
    '''
    return 'to be written'
