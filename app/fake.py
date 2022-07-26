from random import randint, choice
from datetime import date
from faker import Faker
from sqlalchemy.sql.expression import func
from sqlalchemy.exc import IntegrityError
import re
import os
from . import db
from .models import *


faker_lang = os.environ.get('FAKER_LANG') or ''
fake = Faker(faker_lang)


def fake_lifeyears(min_age=18):
    "Ensures rational age of a person."

    while True:
        birth_year = fake.year()
        death_year = fake.year()

        if int(death_year) - int(birth_year) >= min_age:
            return {'text': f'{birth_year}-{death_year}',
                    'birth': int(birth_year),
                    'death': int(death_year)}


def people(count=100):
    i = 0

    while i < count:
        life_years = fake_lifeyears()
        person = Person(forenames=fake.first_name(),
                        last_name=fake.last_name(),
                        note=fake.text(100),
                        life_years=life_years['text'],
                        birth_date=date(life_years['birth'],
                                        randint(1, 12), randint(1, 28)),
                        death_date=date(life_years['death'],
                                        randint(1, 12), randint(1, 28)))

        if life_years['birth'] % 2 == 0:
            for _ in range(0, randint(1, 3)):
                name_variant = PersonNameVariant(
                    first_name_variant=fake.first_name(),
                    last_name_variant=fake.last_name())
                person.name_variants.append(name_variant)

        db.session.add(person)
        i += 1

    db.session.commit()


def geographic_locations(count=100):
    i = 0
    while i < count:
        fake_location = fake.location_on_land()
        name = fake_location[2]
        determiner = fake_location[4]

        if GeographicLocation.query.filter_by(name=name).first():
            continue
        else:
            db.session.add(GeographicLocation(name=name,
                                              determiner=determiner,
                                              note=fake.text(99)))
        i += 1
    db.session.commit()


def collective_bodies(count=100):
    i = 0
    while i < count:
        collectivity_name = fake.company()
        if CollectiveBody.query.filter_by(name=collectivity_name).first():
            continue
        company_abbr = '.'.join(
            [initial[0].upper()
             for initial in re.split(r'\s|\-', collectivity_name)]) + '.'

        collective_body = CollectiveBody(name=collectivity_name,
                                         address=fake.address(),
                                         abbr=company_abbr,
                                         description=fake.text())
        db.session.add(collective_body)
        i += 1
    db.session.commit()


def keywords(count=300):
    i = 0
    while i < count:
        db.session.add(Keyword(keyword=fake.text(15).split()[0],
                               determiner=fake.text(15).split()[0]))
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()


def _entity_list(model, max_repetition=4):
    '''Helper function for documents().
    '''
    __mapper_args__ = {
        'polymorphic_identity':'documents',
        'polymorphic_on': '*'
    }
    entities = []
    iterator = 0
    while iterator < randint(1, max_repetition):
        entity = model.query.order_by(func.random()).first()
        if entity in entities: continue
        entities.append(entity)
        iterator += 1
    return entities


def add_language_subjects(document, max_number=3):
    '''Adds languages as document subjects.
    '''
    i = 0
    while i < randint(1, max_number):
        language_subject = Language.query.order_by(func.random()).first()
        document.language_subjects.append(language_subject)
        db.session.add(document)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            continue
        i += 1


def documents(count=1):
    # opis:
    # Losuje typ dokumentu
    # Jeżeli wylosowany typ to artykuł, losuje periodyk i
    # dodaje powiązane dokumenty (jeżeli się to nie powiedzie-
    # np. kwerenda nie zwróci periodyku, bo ich jeszcze nie ma-wraca
    # do nagłówka pętli)
    # Tworzy autora-osobę (os. losowa)
    # dodaje autora-osobę do dokumentu
    # tworzy tłumacza, korektora (zależy co wylosuje) i dod. do dok.
    # losuje firmę i z wylosowanej firmy tworzy wydawcę i dodaje do dok.
    # dodaje miejsca wydania (1-3)
    #
    # tematy dokumentu (każdy 1-4):
    #
    # Jeżeli tworzony dokument to książka: do niektórych książek
    # dodaje serię (wyszukuje w bazie
    # lub tworzy nazwę w polu uproszczonej serii)
    # Paginacja
    # commit po każdym dodaniu dokumentu

    documents_list = []
    MAX_REPETITION_NUMBER = 4
    i = 0

    while i < count:
        document = Document()
        document.title_proper = fake.text(20)
        document.other_title_inf = fake.text(25)
        document.parallel_title = fake.text(20)
        document.publication_date = fake.year()
        document.note = fake.text()
        document.isbn_10 = fake.isbn10()
        document.isbn_13 = fake.isbn13()
        document.dimensions = f"{randint(10, 50)} cm"
        document.physical_details = choice(
            ['transparency', 'ill.', 'wood', 'various materials'])
        document.pagination = f'[{randint(3, 10)}], {randint(40, 600)} p.'
        document.accompanying_material = choice(
            ['answer book', 'atlas (37 p., 19 leaves : col. maps ; 37 cm.)',
             'reference manual', 'study score', 'art reproduction',
             'film cassette', 'lithograph, black and white'])
        document.edition_statement = (choice(['1st', '2nd', '3nd'])
                                      + ' edition'
                                      + choice([', with minor revisions',
                                                ', third impression',
                                                ', Canadian revision']))
        document.additional_edition_stmt = choice(
            ['Medium voice range',
             'Interactive version',
             'Authorized French language edition',
             'Revised and up-to-date'])

        # potem - na końcu (jeżeli artykuł):

        add_language_subjects(document, 4)
        document_type = DocumentType.query.order_by(func.random()).first()
        if document_type.name == 'article':
            periodical = DocumentType.query.filter_by(
                name='periodical').first()

            # ewentualnie użyć len()
            if periodical.documents.count() == 0:
                continue
            else:
                doc = choice(list(periodical.documents))
                doc.dependent_docs.append(RelatedDocuments(
                    dependent_doc=document,
                    description='Article'))

        resp_author = ResponsibilityName.query.filter_by(
            responsibility_name='author').first()

        document.document_type = document_type

        author_person = Person.query.order_by(func.random()).first()
        author = ResponsibilityPerson(
            responsibility=resp_author,
            person=author_person,
            document=document)

        other_resp_people = [resp_author]
        y = 0
        while y < randint(1, MAX_REPETITION_NUMBER):
            responsibility_person = ResponsibilityName.query.order_by(
                func.random()).first()
            if responsibility_person in other_resp_people:
                continue
            person = Person.query.order_by(func.random()).first()

            other_resp_people.append(
                ResponsibilityPerson(responsibility=responsibility_person,
                                     person=person,
                                     document=document).responsibility)

            y += 1

        publisher_responsibility = ResponsibilityName.query.filter_by(
            responsibility_name='publisher').first()
        publisher_company = CollectiveBody.query.order_by(
            func.random()).first()
        document.responsibility_collectivities.append(
            ResponsibilityCollectivity(
                responsibility=publisher_responsibility,
                collectivity=publisher_company))

        document.publication_places = _entity_list(GeographicLocation)
        document.keywords = _entity_list(Keyword)
        document.subjects_locations = _entity_list(GeographicLocation)
        document.topic_people = _entity_list(Person)
        document.collectivity_subjects = _entity_list(CollectiveBody)

        document_language = Language.query.order_by(func.random()).first()
        original_language = document_language
        while original_language is document_language:
            original_language = Language.query.order_by(func.random()).first()

        document.language = document_language
        document.original_language = original_language

        series = None
        numbering = None        
        if document_type.name == 'book':
            series = ' '.join(fake.text(50).split()[0:3]) + ' series'
            numbering = f"{choice(['Vol.', 'Bd.'])} {randint(1, 90)}"
        document.series = series
        document.numbering = numbering

        db.session.add(document)
        db.session.commit()
        documents_list.append(document)
        i += 1
    return documents_list


def create_all():
    '''Creates new database with fake data.
    '''
    Language.add_languages()
    Role.insert_roles()
    DocumentType.add_basic_document_types()
    ResponsibilityName.add_basic_responsibilities()
    people()
    geographic_locations()
    collective_bodies()
    keywords()
    documents(count=100)
