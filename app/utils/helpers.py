'''Helper classes/functions for the app.
'''

from app import models
from app.models import ResponsibilityName, DocumentType
from flask import request, current_app
from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField

def get_responsibility_identifiers(responsibility_id=None):
    '''Returns tuple with responsibility id and name or redirects to 404 page
    if no responsibility found with a given responsibility_id.
    '''
    if responsibility_id is None: return None, None
    responsibility = ResponsibilityName.query.filter_by(
            id=responsibility_id).first_or_404()

    return responsibility_id, responsibility.responsibility_name


def paginate(query, per_page=0, start_page=0):
    '''Returns default query pagination for view functions.
    '''
    _start_page = start_page or request.args.get('page', 1, type=int)

    return query.paginate(
        _start_page,
        per_page=per_page or current_app.config['LIST_ENTRIES_PER_PAGE'],
        error_out=True)


def get_search_parameters():
    '''Returns search parameters (from the URL query) for documents_list
    view function.
    '''
    search_parameters = {}
    search_parameters['by_entry_type'] = request.args.get(
        'by_entry_type', None)
    search_parameters['filter_type'] = request.args.get(
        'filter_type', None)
    search_parameters['id_number'] = request.args.get(
        'id_number', None, type=int)
    (search_parameters['responsibility_id'],
     responsibility_name) = get_responsibility_identifiers(request.args.get(
         'responsibility_id', None, type=int))

    if any(v for _, v in search_parameters.items()):
        return search_parameters
    else:
        return {}


def select_document_types():
    '''Returns a WTForms form displaying checkboxes with
    document types (on a document list).

    Class requires current request context available during creation and
    for this sake should be called inside a route function.
    '''
    selected_doc_types_ids = request.args.getlist(
        'type_id', type=int)

    class SelectDocumentTypes(FlaskForm):
        for doc in DocumentType.query.order_by(
                DocumentType.name).all():
            locals()[f'doctype_{doc.type_id}'] = BooleanField(
                doc.name.capitalize(),
                id=doc.type_id,
                default='checked' if doc.type_id in
                selected_doc_types_ids
                or not selected_doc_types_ids else '',
                render_kw={'autocomplete': 'off'})
        submit = SubmitField('Apply filter')

        def get_type_ids(document_types_form):
            '''Returns list of selected DocumentType ids.
            '''
            selected_doc_types_ids = []
            for fieldname, value in document_types_form.data.items():
                field_id = str(getattr(document_types_form, fieldname).id)
                if field_id.isnumeric() and value:
                    selected_doc_types_ids.append(int(field_id))
            return selected_doc_types_ids

    return SelectDocumentTypes


def get_es_search_params(model):
    '''Fetches parameters for Elasticsearch query from the POST request.
    '''
    return model.search(
        request.json.get('query', None),
        request.json.get('page', 1),
        current_app.config['SHORT_LIST_ENTRIES_PER_PAGE'])


def get_query_list(model):
    '''Returns list of items from the SQLAlchemy model
    searched using Elasticsearch.

    Returned items can be serialized into JSON for use
    in search templates.
    model - SQLAlchemy, Elasticsearch searchable model from models.py
    '''
    query, _ = get_es_search_params(model)
    return [{'text': item,
             'id': item.id} for item in query]


def search_multiple_models(models):
    '''Searches multiple models from the database and returns
    combined lists (each made by get_query_list)
    of results with source specified by a tablename.
    '''
    combined_lists = []
    for model in models:
        combined_lists.extend(
            [{'text': item['text'],
              'id': item['id'],
              'source': model.__tablename__}
             for item in get_query_list(model)])
    return combined_lists
