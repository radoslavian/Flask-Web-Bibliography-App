'''Helper classes/functions for the app.
'''

from app import models
from app.models import ResponsibilityName, DocumentType
from flask import request, current_app, jsonify
from flask_wtf import FlaskForm
from wtforms import (BooleanField, SubmitField, SelectField, StringField,
                     validators)

def get_responsibility_identifiers(responsibility_id=None):
    '''Returns tuple with responsibility id and name or redirects to 404 page
    if no responsibility with a given responsibility_id was found.
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


class UnambiguousSearchFields(FlaskForm):
    def __init__(self, *args, **kwargs):
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(UnambiguousSearchFields, self).__init__(*args, **kwargs)

    select_field = SelectField('Select field',
                               choices=['ISBN-10', 'ISBN-13', 'ISSN'],
                               render_kw={'class': 'form-control'})
    search_field = StringField(
        'Enter number', validators=[
            validators.DataRequired('Enter number (with hyphens)'),
            validators.Regexp('^[\d-]+$')],
        render_kw={'class': 'form-control',
                   'type': 'text',
                   'data-toggle': 'tooltip',
                   'title': 'Enter searched number with hyphens.'})
    submit = SubmitField('Search',
                         render_kw={'class': 'btn btn-primary'})


class QuickSearchForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(QuickSearchForm, self).__init__(*args, **kwargs)

    q = StringField(validators=[validators.DataRequired()],
                    render_kw={'class': 'form-control w-100',
                               'placeholder': 'Full text quick-search',
                               'data-toggle': 'tooltip',
                               'size': 40,
                               'title': '''Search for documents,
			       personal/geographic/
			       collective names and subject keywords.'''})
    search = SubmitField('Search',
                         render_kw={'class': 'btn btn-success mr-3'})


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


def get_jsonified(model):
    '''Helper for get_... view functions called from search pages.
    Returns jsonified database model(s).
    '''
    id_number = request.json.get('id', None)
    if id_number:
        return jsonify(model.query.filter(
            getattr(model, model.__primary_key__) == id_number).first())
    return jsonify(get_query_list(model))


def get_es_search_params(model, page=1):
    '''Fetches parameters for Elasticsearch query from the POST request.
    '''
    return model.search(
        request.json.get('query', None),
        request.json.get('page', page),
        current_app.config['SHORT_LIST_ENTRIES_PER_PAGE'])


def get_query_list(model, page=1):
    '''Returns list of items from the SQLAlchemy model
    searched using Elasticsearch.

    Returned items can be serialized into JSON for use
    in search templates.
    model - SQLAlchemy, Elasticsearch searchable model from models.py
    '''
    query, total = get_es_search_params(model, page)
    next_page =  total > (page * current_app.config[
        'SHORT_LIST_ENTRIES_PER_PAGE'])

    return [{'text': item,
             'id': item.id} for item in query], next_page


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
