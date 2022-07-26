"""Dynamic list constructor functions for route breadcrumbs."""

from ..models import (User, Language, DocumentType, CollectiveBody,
                      GeographicLocation, Keyword, ResponsibilityName, Person,
                      PersonNameVariant, Document)
from flask import abort, request, url_for


def user_dlc(*args, **kwargs):
    """Dynamic list constructor for the user() breadcrumb."""

    username = request.view_args.get('username', None)
    user = User.query.filter_by(username=username).first()
    text = user.name or user.username or f'User id: {user.user_id}'
    return [{'text': text,
             'url': url_for('main.user', username=username)}]


# TODO: create view_utils module for such functionality
documents = {
    'description': ('Project description', '_project_description.html'),
    'technologies-used': ('Technologies used',
                          '_technologies_used.html'),
    'references': ('References', '_references.html')
}


def main_page_dlc(*args, **kwargs):
    """Dynamic list constructor for main page subpages."""

    document_key = request.view_args.get('document', None)
    text = documents.get(document_key, None)[0]
    url = url_for('main.main_page', document=document_key)

    return [{'text': text, 'url': url}]


def edit_database_entry_dlc(*args, **kwargs):
    model_name = request.view_args.get('model_name', None)
    new_entry = request.args.get('new', False)
    entry_id = request.args.get('id', None)

    item = {
        'language': lambda: {
            'list_text': 'Languages',
            'list_url': url_for('main.language_list'),
            'entry_text': (Language.query.get(entry_id)
                           if entry_id else 'Add new entry'),
            'entry_url': (
                {
                    'endpoint': 'main.language_details',
                    'language_id': entry_id
                } if entry_id else {
                    'endpoint': 'main.edit_database_entry',
                    'model_name': 'language',
                    'new': True
                }
            )
        },
        'document-type': lambda: {
            'list_text': 'Document types',
            'list_url': url_for('main.document_types_list'),
            'entry_text': (DocumentType.query.get(entry_id)
                           if entry_id else 'Add new entry'),
            'entry_url': (
                {
                    'endpoint': 'main.document_type',
                    'type_id': entry_id
                } if entry_id else {
                    'endpoint': 'main.edit_database_entry',
                    'model_name': 'document_type',
                    'new': True
                }
            )
        },
        'collective-body': lambda: {
            'list_text': 'Collective names',
            'list_url': url_for('main.collective_bodies_list'),
            'entry_text': (CollectiveBody.query.get(entry_id)
                           if entry_id else 'Add new entry'),
            'entry_url': (
                {
                    'endpoint': 'main.collective_body_details',
                    'c_body_id': entry_id
                } if entry_id else {
                    'endpoint': 'main.edit_database_entry',
                    'model_name': 'collective_body',
                    'new': True
                }
            )
        },
        'geographic-location': lambda: {
            'list_text': 'Geographic locations',
            'list_url': url_for('main.geographic_locations_list'),
            'entry_text': (GeographicLocation.query.get(entry_id)
                           if entry_id else 'Add new entry'),
            'entry_url': (
                {
                    'endpoint': 'main.geographic_location_details',
                    'location_id': entry_id
                } if entry_id else {
                    'endpoint': 'main.edit_database_entry',
                    'model_name': 'geographic_location',
                    'new': True
                }
            )
        },
        'subject-keyword': lambda: {
            'list_text': 'Subject keywords',
            'list_url': url_for('main.keywords_list'),
            'entry_text': (Keyword.query.get(entry_id)
                           if entry_id else 'Add new entry'),
            'entry_url': (
                {
                    'endpoint': 'main.keyword_details',
                    'keyword_id': entry_id
                } if entry_id else {
                    'endpoint': 'main.edit_database_entry',
                    'model_name': 'keyword',
                    'new': True
                }
            )
        },
        'responsibility-name': lambda: {
            'list_text': 'Document responsibilities',
            'list_url': url_for('main.responsibilities_list'),
            'entry_text': (ResponsibilityName.query.get(entry_id)
                           if entry_id else 'Add new entry'),
            'entry_url': (
                {
                    'endpoint': 'main.responsibility_details',
                    'responsibility_id': entry_id
                } if entry_id else {
                    'endpoint': 'main.edit_database_entry',
                    'model_name': 'responsibility-name',
                    'new': True
                }
            )
        },
        'person-name': lambda: {
            'list_text': 'People',
            'list_url': url_for('main.browse_people'),
            'entry_text': (Person.query.get(entry_id)
                           if entry_id else 'Add new entry'),
            'entry_url': (
                {
                    'endpoint': 'main.person_details',
                    'person_id': entry_id
                } if entry_id else {
                    'endpoint': 'main.edit_database_entry',
                    'model_name': 'person-name',
                    'new': True
                }
            )
        },
        'person-name-variant': lambda: {
            'list_text': 'People',
            'list_url': url_for('main.browse_people'),
            'entry_text': (str(PersonNameVariant.query.get(entry_id))
                           if entry_id else 'Add new entry'),
            'entry_url': (
                {
                    'endpoint': 'main.name_variant',
                    'variant_id': entry_id
                } if entry_id else {
                    'endpoint': 'main.edit_database_entry',
                    'model_name': 'person-name-variant',
                    'new': True
                }
            )
        },
        'document': lambda: {
            'list_text': 'Documents',
            'list_url': url_for('main.documents_list'),
            'entry_text': (Document.query.get(
                entry_id).title_proper.rstrip('.')
                           if entry_id else 'Add new entry'),
            'entry_url': (
                {
                    'endpoint': 'main.document_view',
                    'document_id': entry_id
                } if entry_id else {
                    'endpoint': 'main.edit_database_entry',
                    'model_name': 'document',
                    'new': True
                }
            )
        }
    }.get(model_name, lambda: abort(404))()

    breadcrumbs = [
        {
            'text': item['list_text'],
            'url': item['list_url']
        },  # list breadcrumb
        {
            'text': item['entry_text'],
            'url': url_for(**item['entry_url'])
        }  # item (language, document etc.) breadcrumb
    ]
    if not new_entry and entry_id:
        # optional 'Edit' entry breadcrumb
        breadcrumbs.append({'text': 'Edit',
                            'url': url_for('main.edit_database_entry',
                                           model_name=model_name,
                                           id=entry_id)})
    return breadcrumbs


def document_dlc(*args, **kwargs):
    document_id = request.view_args.get('document_id', None)
    document = Document.query.get(document_id)

    return [{'text': document.title_proper.rstrip('.'),
             'url': url_for('main.document_view',
                            document_id=document.document_id)}]


def geographic_location_details_dlc(*args, **kwargs):
    """Dynamic list constructor for geographic location details endpoint."""

    location_id = request.view_args.get("location_id", None)
    location = GeographicLocation.query.get(location_id)

    return [{"text": location.name.capitalize(),
             "url": url_for("main.geographic_location_details",
                            location_id=location_id)}]


def keyword_details_dlc(*args, **kwargs):
    """Dynamic list constructor for keyword details endpoint."""

    keyword_id = request.view_args.get("keyword_id")
    keyword = Keyword.query.get(keyword_id)

    return [{'text': str(keyword),
             'url': url_for('main.keyword_details',
                            keyword_id=keyword_id)}]


def language_details_dlc(*args, **kwargs):
    language_id = request.view_args.get('language_id', None)
    language = Language.query.get(language_id)

    return [{"text": str(language),
             "url": url_for('main.language_details',
                            language_id=language_id)}]


def name_variant_dlc(*args, **kwargs):
    variant_id = request.view_args.get('variant_id', None)
    variant = PersonNameVariant.query.get(variant_id)

    return [{"text": str(variant),
             "url": url_for('main.name_variant',
                            variant_id=variant_id)}]


def person_details_dlc(*args, **kwargs):
    person_id = request.view_args.get('person_id', None)
    person = Person.query.get(person_id)

    return [{"text": str(person),
             "url": url_for('main.person_details',
                            person_id=person_id)}]


def responsibility_details_dlc(*args, **kwargs):
    responsibility_id = request.view_args.get('responsibility_id', None)
    responsibility = ResponsibilityName.query.get(responsibility_id)

    return [{"text": str(responsibility),
             "url": url_for('main.responsibility_details',
                            responsibility_id=responsibility_id)}]


def collective_body_dlc(*args, **kwargs):
    c_body_id = request.view_args.get('c_body_id')
    collective_body_record = CollectiveBody.query.filter_by(
        id=c_body_id).first()

    return [{'text': collective_body_record.name,
             'url': url_for('main.collective_body_details',
                            c_body_id=c_body_id)}]


def document_type_dlc(*args, **kwargs):
    document_type = DocumentType.query.filter_by(
        type_id=request.view_args.get('type_id')).first()

    return [{'text': document_type.name.capitalize(),
             'url': url_for('main.document_type', type_id=document_type.id)}]
