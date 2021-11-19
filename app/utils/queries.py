'''Queries that require separate functions.
'''

from app.models import *
from app.utils.helpers import get_responsibility_identifiers
from flask import abort
from app import db

def list_people_name_variants():
    '''Returns query of people and name variant entries from the database
    (with common field names).
    '''
    people = ResponsibilityPerson.query.with_entities(
            Person.person_id,
            Person.forenames,
            Person.last_name,
            Person.life_years)
    name_variants = PersonNameVariant.query.with_entities(
            PersonNameVariant.variant_id,
            PersonNameVariant.first_name_variant,
            PersonNameVariant.last_name_variant,
            db.literal('name_variant'))

    return people.union_all(name_variants).order_by(
        Person.last_name.asc(), Person.forenames.asc())


def collective_body_entry(search_parameters):
    '''Returns query for documents_list where search entry is
    a collective body.
    '''
    collective_body = CollectiveBody.query.filter_by(
        id=search_parameters['id_number']).first_or_404()
    subtitle = ''

    if search_parameters['filter_type'] == 'by_subject':
        query = collective_body.documents_topics
        subtitle = f'''Documents where collective body
        <em>{collective_body.name}</em> is a subject.'''

    elif search_parameters['filter_type'] == 'by_responsibility':
        _, responsibility_name = get_responsibility_identifiers(
            search_parameters['responsibility_id'])

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
        <em>{responsibility_name.capitalize()}</em>:'''

    else:
        abort(404)

    return query, subtitle


def person_entry(search_parameters):
    '''Returns query for documents_list where search entry is
    a person (as a subject or responsibility holder).
    '''
    person = Person.query.filter_by(
        person_id=search_parameters['id_number']).first_or_404()

    if search_parameters['filter_type'] == 'by_subject':
        query = person.documents_topics
        subtitle = f'''Documents where an individual name
        <em>{person.forenames} {person.last_name}</em> is a subject.'''

    elif search_parameters['filter_type'] == 'by_responsibility':
        _, responsibility_name = get_responsibility_identifiers(
        search_parameters['responsibility_id'])
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
        abort(404)
    return query, subtitle


def geographic_location_entry(search_parameters):
    '''Returns query for documents_list where search entry is
    geographic location.
    '''
    geographic_location = GeographicLocation.query.filter_by(
            location_id=search_parameters['id_number']).first_or_404()

    if search_parameters['filter_type'] == 'by_publication_place':
        query = geographic_location.document_publication_place
        subtitle = f'''Documents published in
        <em>{geographic_location.name}:</em>'''

    elif search_parameters['filter_type'] == 'by_subject':
        query = geographic_location.documents_topics
        subtitle = f'''Documents where <em>{geographic_location.name}
        </em> is a subject:'''

    else:
        abort(404)

    return query, subtitle


def subject_keyword_entry(search_parameters):
    '''Returns query for documents_list where search entry is
    subject keyword.
    '''
    keyword_entry = Keyword.query.filter_by(
        id=search_parameters['id_number']).first_or_404()
    query = keyword_entry.documents
    subtitle = f'''Documents where keyword
    <em>{keyword_entry.keyword}</em> is a subject:'''

    return query, subtitle


def language_entry(search_parameters):
    '''Returns query for documents_list where language is a search entry.
    '''
    language = Language.query.filter_by(
        language_id=search_parameters['id_number']).first_or_404()

    if search_parameters['filter_type'] == 'by_publication_language':
        query = language.documents
        subtitle = f'''Documents published in
        <em>{language.language_name}</em> language:'''

    elif search_parameters['filter_type'] == 'by_original_language':
        query = language.documents_original_lang
        subtitle = f'''Documents for which
        <em>{language.language_name}</em> is an original language:'''

    elif search_parameters['filter_type'] == 'by_topic':
        query = language.documents_topics
        subtitle = f'''Documents where
        <em>{language.language_name}</em> language is a topic:'''

    else:
        abort(404)

    return query, subtitle


query_pattern_matching = {
    # dictionary for pattern matching in views.documents_list()
    #
    'collective_body'     : collective_body_entry,
    'person'              : person_entry,
    'geographic_location' : geographic_location_entry,
    'subject_keyword'     : subject_keyword_entry,
    'language'            : language_entry
}


# queries for document search route
def document_search_people():
    pass
    # db.session.query(Document).select_from(Document)
