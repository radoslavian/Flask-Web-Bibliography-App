"""View functions for the the application main blueprint.
"""

__name__ = 'views'

from . import main
from flask import (render_template, session,
                   redirect, url_for, jsonify, flash, g)
from flask_login import login_required
from app import db
from app.utils import queries
from flask_breadcrumbs import register_breadcrumb
from ..models import *
from app.utils.decorators import *
from app.utils.helpers import *
from app.utils.queries import *
from app.utils.app_utils import *
from app.main.forms import *
from app.main.dynamic_list_constructors import *


@main.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
    g.search_form = QuickSearchForm()


@main.route('/user-list')
@register_breadcrumb(main, '.user_list', 'User list')
@login_required
@admin_required
def user_list():
    users = User.query.order_by(User.name)
    return render_template(
        'list_of_items.html',
        title='List of users',
        subtitle='Alphabetical order, ascending',
        pagination=paginate(users),
        endpoint='.user_list',
        partial_template_name='_user_list.html')


@main.route('/user/<username>')
@login_required
@register_breadcrumb(main, '.user_list.user', 'User',
                     dynamic_list_constructor=user_dlc)
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user_profile.html', user=user)


@main.route('/edit-profile/<username>', methods=['GET', 'POST'])
@login_required
@admin_required
@register_breadcrumb(main, '.user_list.user.edit_profile', 'Edit profile')
def edit_profile(username):
    '''User profile editing for administrator.
    '''
    user = User.query.filter_by(username=username).first_or_404()
    edit_form = EditProfileForm(obj=user, user=user)
    if edit_form.validate_on_submit():
        edit_form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        flash('User profile successfully updated!')
        return redirect(url_for('main.user', username=user.username))
    return render_template('edit_profile.html',
                           edit_form=edit_form, user=user)


@main.route('/edit/<model_name>/', methods=['GET', 'POST'])
@login_required
@permission_required(Permissions.EDIT_BIBLIOGRAPHY)
@register_breadcrumb(main, '.edit_database_entry', 'Add new entry',
                     dynamic_list_constructor=edit_database_entry_dlc)
def edit_database_entry(model_name):
    models = {
        # model bd może iść do konstruktora ModelEditForm
        # + zmiany w tej funkcji (łatwiej będzie to zrobić
        # jak będę miał test automatyczny)
        'language': [LanguageEditForm, Language],
        'document-type': [DocumentTypeEditForm, DocumentType],
        'collective-body': [CollectiveBodyEditForm, CollectiveBody],
        'geographic-location': [GeographicLocationEditForm,
                                GeographicLocation],
        'subject-keyword': [KeywordEditForm, Keyword],
        'responsibility-name': [ResponsibilityNameEditForm,
                                ResponsibilityName],
        'person-name': [PersonEditForm, Person],
        'person-name-variant': [PersonNameVariantEditForm,
                                PersonNameVariant],
        'document': [DocumentEditForm, Document]
    }
    if model_name not in models:
        abort(404)
    else:
        model_form = models[model_name][0]
        model = models[model_name][1]

    options = {}
    if model_name == 'person-name':
        template = 'edit_person_details.html'
    elif model_name == 'document':
        template = 'edit_document_details.html'
        options['ordering_range'] = 10
    else:
        template = 'edit_entity.html'

    id_number = request.args.get('id', None)
    if id_number:
        entity_form = model_form(obj=model.query.get_or_404(id_number))
    elif request.args.get('new') == 'True':
        entity_form = model_form()
    else:
        abort(404)
    if entity_form.validate_on_submit():
        if entity_form.commit_row():
            return redirect(url_for(**entity_form.redirect_to()))

    return render_template(template, entity_form=entity_form, options=options)


@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403


@main.route('/browse/people/')
@register_breadcrumb(main, '.browse_people', 'People')
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


@main.route('/browse/documents/id=<document_id>')
@register_breadcrumb(main, '.documents_list.document_view', 'Document',
                     dynamic_list_constructor=document_dlc)
def document_view(document_id):
    document = Document.query.filter_by(
        document_id=document_id).first_or_404()

    sort = {
        'responsibilities_collectivities': lambda resp_col: sorted(
            resp_col,
            key=lambda item: (
                item.ordering,
                item.collectivity.name)),
        'responsibilities_individuals': lambda resp_ind: sorted(
            resp_ind,
            key=lambda item: (
                item.ordering,
                item.person.last_name or item.person.forenames)),
        'dependent_docs': lambda doc: sorted(
            doc,
            key=lambda item: (
                item.ordering,
                item.dependent_doc.title_proper))
    }

    return render_template('document.html', document=document, sort=sort)


@main.route('/browse/geographic-locations/id=<location_id>')
@register_breadcrumb(
    main, '.geographic_locations_list.geographic_location_details',
    'Geographic location details',
    dynamic_list_constructor=geographic_location_details_dlc)
def geographic_location_details(location_id):
    location = GeographicLocation.query.filter_by(
        location_id=location_id).first_or_404()

    return render_template('geographic_location_details.html',
                           location=location)


@register_breadcrumb(main, '.geographic_locations_list',
                     'Geographic locations')
@main.route('/browse/geographic-locations/')
def geographic_locations_list():
    locations = GeographicLocation.query.order_by(GeographicLocation.name)

    return render_template(
        'geographic_locations_list.html',
        title='List of geographic locations',
        subtitle='Ordered alphabetically, ascending.',
        pagination=paginate(locations),
        endpoint='.geographic_locations_list')


@main.route('/')
@register_breadcrumb(main, '.', 'Main')
def index():
    return main_page('description')


@main.route('/<document>/')
@register_breadcrumb(main, '.document', 'Document',
                     dynamic_list_constructor=main_page_dlc)
def main_page(document):
    if document not in documents:
        abort(404)

    return render_template('document_page.html',
                           documents=documents,
                           document=document)


@main.route('/browse/keywords/id=<keyword_id>')
@register_breadcrumb(main, '.keywords.keyword_details',
                     'Keyword details',
                     dynamic_list_constructor=keyword_details_dlc)
def keyword_details(keyword_id):
    keyword = Keyword.query.filter_by(id=keyword_id).first_or_404()

    return render_template('keyword_details_view.html',
                           keyword=keyword)


@main.route('/browse/keywords/')
@register_breadcrumb(main, '.keywords', 'Subject keywords')
def keywords_list():
    keywords = Keyword.query.order_by(Keyword.keyword)

    return render_template('keywords_list.html',
                           title='List of subject headers from the database',
                           subtitle='Ordered alphabetically, ascending.',
                           pagination=paginate(keywords),
                           endpoint='.keywords_list')


@main.route('/browse/languages/')
@register_breadcrumb(main, '.languages', 'Languages')
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
@register_breadcrumb(main, '.languages.language_details',
                     'Language details',
                     dynamic_list_constructor=language_details_dlc)
def language_details(language_id):
    language = Language.query.filter_by(
        language_id=language_id).first_or_404()

    return render_template('language_details.html',
                           language=language)


@main.route('/browse/people/name-variants/id=<variant_id>')
@register_breadcrumb(main, '.browse_people.name_variant', 'Name variant',
                     dynamic_list_constructor=name_variant_dlc)
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
    # move it into utils
    return {responsibility_person.responsibility
            for responsibility_person in item_responsibilities}


def responsibility_list(responsibilities, query_fn):
    '''Lists responsibilities from a collective body or person relationship
    field and counts number of documents for each one
    in which a given entity appears with a particular responsibility.
    '''

    # move it into utils
    responsibilities_list = []
    for responsibility in responsibilities:
        resp_count = query_fn(responsibility).count()
        responsibilities_list.append(
            [responsibility, resp_count])
    responsibilities_list.sort(key=lambda item: item[0].responsibility_name)

    return responsibilities_list


@main.route('/browse/people/id=<person_id>')
@register_breadcrumb(main, '.browse_people.person_details',
                     'Person details',
                     dynamic_list_constructor=person_details_dlc)
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
@register_breadcrumb(main, '.responsibilities_list',
                     'Document responsibilities')
def responsibilities_list():
    responsibilities = ResponsibilityName.query.order_by(
        ResponsibilityName.responsibility_name)

    return render_template(
        'list_of_items.html',
        responsibilities=responsibilities,
        title='List of document responsibilities',
        subtitle='Alphabetical order, ascending',
        partial_template_name='_responsibilities.html')


@main.route('/browse/responsibilities/id=<responsibility_id>')
@register_breadcrumb(main, '.responsibilities_list.responsibility_details',
                     'Responsibility details',
                     dynamic_list_constructor=responsibility_details_dlc)
def responsibility_details(responsibility_id):
    # change to get_or_404
    responsibility = ResponsibilityName.query.filter_by(
        id=responsibility_id).first_or_404()

    return render_template('responsibility_details.html',
                           responsibility=responsibility)


@main.route('/browse/collective-bodies/id=<c_body_id>')
@register_breadcrumb(main, '.collective_bodies_list.collective_body_details',
                     'Collective names',
                     dynamic_list_constructor=collective_body_dlc)
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
@register_breadcrumb(main, '.collective_bodies_list', 'Collective names')
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
@register_breadcrumb(main,
                     '.document_types_list.document_type',
                     'Document type',
                     dynamic_list_constructor=document_type_dlc)
def document_type(type_id):
    '''Route for details of the document type entry from
    the database, identified by type_id.
    '''
    document_type = DocumentType.query.filter_by(
        type_id=type_id).first_or_404()

    return render_template('document_type_details.html',
                           document_type=document_type)


@main.route('/browse/document-types/')
@register_breadcrumb(main, '.document_types_list', 'Document types')
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


@main.route('/browse/documents/', methods=['GET', 'POST'])
@register_breadcrumb(main, '.documents_list', 'Documents')
def documents_list():
    start_page = 0
    document_types_form = select_document_types()(id='myform')
    selected_doc_types_ids = document_types_form.get_type_ids()
    search_parameters = get_search_parameters()
    subtitle = None

    if session.get(
            'prev_selected_doc_types_ids') != selected_doc_types_ids:
        start_page = 1
        session['prev_selected_doc_types_ids'] = selected_doc_types_ids

    kargs = {**search_parameters,
             'type_id': selected_doc_types_ids}
    if request.method == 'POST':
        return redirect(url_for('.documents_list', **kargs))

    query_fn = query_pattern_matching.get(
        search_parameters.get('by_entry_type'))

    if query_fn:
        query, subtitle = query_fn(search_parameters)
    else:
        query = Document.query

    if len(selected_doc_types_ids) != DocumentType.query.count():
        query = query.filter(Document.document_type_id.in_(
            selected_doc_types_ids))
    query = query.order_by(Document.title_proper)

    return render_template(
        'list_of_items.html',
        kargs=kargs,
        subtitle=subtitle,
        pagination=paginate(query, start_page=start_page),
        document_types=document_types_form,
        title='List of the document titles from the database',
        partial_template_name='_documents_list.html',
        endpoint='.documents_list')


@main.route('/search/people/', methods=['POST'])
def get_person_entries():
    '''Returns JSON Array of <number> entries, on a <page_num> page.
    '''
    page = request.json.get('page', 1)
    person_id = request.json.get('id', None)
    if person_id:
        return jsonify(Person.query.filter_by(
            person_id=person_id).first())

    output_people, next_page_people = get_query_list(Person, page)
    variants, total_variants = get_es_search_params(PersonNameVariant)
    next_page_variants = total_variants > (page * current_app.config[
        'SHORT_LIST_ENTRIES_PER_PAGE'])

    # filter only name variants referenced by a main person name
    output_variants = (
        {'text': item,
         'id': item.person_id} for item in
        filter(lambda variant: variant.person_id, variants))
    output_people.extend(output_variants)

    return jsonify(output_people,
                   # czy poniżej muszą być nawiasy?
                   (next_page_people or next_page_variants))


# można zrobić jedną trasę dla wszystkich z elementem dynamicznym
# np. /search/<entries>/
@main.route('/search/keywords', methods=['POST'])
def get_keywords():
    return get_jsonified(Keyword)


@main.route('/search/geographic_locations', methods=['POST'])
def get_geographic_location():
    return get_jsonified(GeographicLocation)


@main.route('/search/collective_bodies', methods=['POST'])
def get_collective_bodies():
    return get_jsonified(CollectiveBody)


@main.route('/search/name-variant', methods=['POST'])
def get_name_variant():
    query = get_es_search_params(PersonNameVariant)
    print([item.id for item in query[0]])
    return jsonify([{'text': str(query_item) + f' (id {query_item.id})',
                     'id': query_item.id} for query_item in query[0]])


@main.route('/search/documents', methods=['POST'])
def get_documents():
    return get_jsonified(Document)


@main.route('/search/languages', methods=['POST'])
def get_language_entries():
    '''Returns json array of languages searched in the db using
    search engine.
    '''
    return get_jsonified(Language)


search_parameters = {
    'responsibility_person_id':
    document_search_responsibility_area(
        ResponsibilityPerson, 'person_id'),
    'responsibility_collectivity_id':
    document_search_responsibility_area(
        ResponsibilityCollectivity, 'collectivity_id'),
    'topic_person_id': query_documents(
        Person, 'documents_topics'),
    'publication_language_id' : query_documents(
        Language, 'documents'),
    'original_language_id' : query_documents(
        Language, 'documents_original_lang'),
    'keyword_id': query_documents(
        Keyword, 'documents'),
    'publication_place_id' : query_documents(
        GeographicLocation, 'document_publication_place'),
    'topic_place_id': query_documents(
        GeographicLocation, 'documents_topics'),
    'collectivity_topic_id': query_documents(
        CollectiveBody, 'documents_topics'),
    'topic_language_id': query_documents(
        Language, 'documents_topics')
}


# function requires some work/improvements
@main.route('/document-search', methods=['GET', 'POST'])
@register_breadcrumb(main, '.document_search', 'Document search')
def document_search():
    start_page = 0
    document_types_form = select_document_types()(id='myform')
    selected_doc_types_ids = document_types_form.get_type_ids()
    unambiguous_fields = UnambiguousSearchFields(request.args)

    if session.get(
            'prev_selected_doc_types_ids') != selected_doc_types_ids:
        start_page = 1
        session['prev_selected_doc_types_ids'] = selected_doc_types_ids

    document_query = ''
    document_queries = []
    received_parameters = {}

    if unambiguous_fields.validate():
        def query_fn(field):
            return Document.query.filter(
                field == unambiguous_fields.search_field.data)

        if unambiguous_fields.select_field.data == 'ISBN-10':
            document_queries.append(query_fn(Document.isbn_10))
        elif unambiguous_fields.select_field.data == 'ISBN-13':
            document_queries.append(query_fn(Document.isbn_13))
        elif unambiguous_fields.select_field.data == 'ISSN':
            document_queries.append(query_fn(Document.issn))
        received_parameters['select_field'] = request.args.get(
            'select_field')
        received_parameters['search_field'] = request.args.get(
            'search_field')
    else:
        for parameter in search_parameters.keys():
            ids = request.args.getlist(parameter, type=int)
            if ids:
                received_parameters[parameter] = ids
                document_queries.append(search_parameters[parameter](ids))
        document_text_search = request.args.get('document_text_search')

        if document_text_search:
            received_parameters['document_text_search'] = document_text_search
            document_query = Document.search(document_text_search, 1,
                                             10000)[0] # ESearch limit

    kargs = {**received_parameters,
             'type_id': selected_doc_types_ids}

    if request.method == 'POST':
        return redirect(url_for('.document_search', **kargs))
    if document_query:
        document_queries.append(document_query.order_by(None))

    if len(document_queries) == 1:
        query = document_queries[0]
    elif len(document_queries) > 1:
        query = document_queries[0].intersect(
            *[document_q for document_q in document_queries[1:]])
    else:
        query = Document.query.filter_by(document_id=0)

    if len(selected_doc_types_ids) != DocumentType.query.count():
        query = query.filter(Document.document_type_id.in_(
            selected_doc_types_ids))

    return render_template('document_search.html',
                           pagination=paginate(query, start_page=start_page),
                           document_types=document_types_form,
                           search_fields=search_fields,
                           kargs=kargs,
                           endpoint='.document_search',
                           unambiguous_fields=unambiguous_fields)


@main.route('/quick-search')
@register_breadcrumb(main, '.quick_search', 'Quick search results')
def quick_search():
    result_fields = [
        {
	    'title': 'Documents found (only title fields ' +
            'are being searched):',
	    'results_id': 'documents',
	    'endpoint': '.get_documents',
            'path': '/browse/documents/'
        },
        {
	    'title': 'Person entries found:',
	    'results_id': 'people', # div with search results
	    'endpoint': '.get_person_entries', # ajax endpoint
            'path': '/browse/people/'
        },
        {
	    'title': 'Collective names found:',
	    'results_id': 'collective_bodies',
	    'endpoint': '.get_collective_bodies',
            'path': '/browse/collective-bodies/'
        },
        {
	    'title': 'Geographic locations found:',
	    'results_id': 'geographic_locations',
	    'endpoint': '.get_geographic_location',
            'path': '/browse/geographic-locations/'
        },
        {
            'title': 'Subject headers (keywords) found:',
            'results_id': 'subject_keywords',
            'endpoint': '.get_keywords',
            'path': '/browse/keywords/'
        },
        {
	    'title': 'Language entries found:',
	    'results_id': 'languages',
	    'endpoint': '.get_language_entries',
            'path': '/browse/languages/'
        }
    ]

    if not g.search_form.validate():
        return redirect(url_for('main.index'))

    return render_template('quick_search_results.html',
                           search_term=g.search_form.q.data,
                           result_fields=result_fields)


@main.route('/delete/<entry_model>/')
@login_required
@permission_required(Permissions.EDIT_BIBLIOGRAPHY)
def delete_entry(entry_model):
    id_number = request.args.get('id', None)
    if not id_number:
        abort(404)
    choice_list = {
        'collective-body': {
            'model': CollectiveBody,
            'endpoint': 'main.collective_body_details',
            'arg': 'c_body_id',
            'list_endpoint': 'main.collective_bodies_list'
        },
        'document-type': {
            'model': DocumentType,
            'endpoint': 'main.document_type',
            'arg': 'type_id',
            'list_endpoint': 'main.document_types_list'
        },
        'document': {
            'model': Document,
            'endpoint': 'main.document_view',
            'arg': 'document_id',
            'list_endpoint': 'main.documents_list'
        },
        'geographic-location': {
            'model': GeographicLocation,
            'endpoint': 'main.geographic_location_details',
            'arg': 'location_id',
            'list_endpoint': 'main.geographic_locations_list'
        },
        'subject-keyword': {
            'model': Keyword,
            'endpoint': 'main.keyword_details',
            'arg': 'keyword_id',
            'list_endpoint': 'main.keywords_list'
        },
        'language': {
            'model': Language,
            'endpoint': 'main.language_details',
            'arg': 'language_id',
            'list_endpoint': 'main.language_list'
        },
        'person-name': {
            'model': Person,
            'endpoint': 'main.person_details',
            'arg': 'person_id',
            'list_endpoint': 'main.browse_people'
        },
        'person-name-variant': {
            'model': PersonNameVariant,
            'endpoint': 'main.name_variant',
            'arg': 'person_id',
            'list_endpoint': 'main.browse_people'
        },
        'responsibility-name': {
            'model': ResponsibilityName,
            'endpoint': 'main.responsibility_details',
            'arg': 'responsibility_id',
            'list_endpoint': 'main.responsibilities_list'
        }
    }
    if entry_model in choice_list:
        selection = choice_list[entry_model]
        error_message = delete_entry_from_db(selection['model'], id_number)
        if error_message:
            flash(f'''Failed to delete entry: {error_message} - before
            attempting to delete an entry, check if it has all
            relationships cleared.''')
            return redirect(url_for(selection['endpoint'],
                                    **{selection['arg']: id_number}))
    else:
        abort(404)

    flash('Entry successfully removed.')
    return redirect(url_for(selection['list_endpoint']))

@main.route('/disclaimer')
@register_breadcrumb(main, '.disclaimer', 'Disclaimer')
def disclaimer():
    return render_template('disclaimer.html')
