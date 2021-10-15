from random import randint
from datetime import date
from faker import Faker
from  sqlalchemy.sql.expression import func
from sqlalchemy.exc import IntegrityError
import re
from . import db
from .models import *

fake = Faker()

def people(count=100):
    i = 0

    def fake_lifeyears(min_age=18):
        "Ensures rational age of a person."

        while True:
            birth_year = fake.year()
            death_year = fake.year()

            if int(death_year) - int(birth_year) >= min_age:
                return {'text': f'{birth_year}-{death_year}',
                        'birth': int(birth_year),
                        'death': int(death_year)}

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
    for _ in range(count):
        collectivity_name = fake.company()
        company_abbr = '.'.join(
            [initial[0].upper()
             for initial in re.split(r'\s|\-', collectivity_name)]) + '.'

        collective_body = CollectiveBody(name=collectivity_name,
                                         address=fake.address(),
                                         abbr=company_abbr,
                                         description=fake.text())
        db.session.add(collective_body)
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


def documents(count=100):
    i = 0

    # losowanie el. z kwerendy
    # from  sqlalchemy.sql.expression import func, select
    # Person.query.order_by(func.random()).first()
    # commit po każdym dodaniu dokumentu
    #
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
    # tematy dokumentu (każdy 1-4)
    # tematy-miejsca (lokalizacja geograficzna)
    # tematy-ludzie
    # tematy-słowa kluczowe
    # tematy-ciała zbiorowe
    #
    # Język dokumentu
    # J. oryginału
    #
    # Jeżeli tworzony dokument to książka, dodaje serię (wyszukuje w bazie
    # lub tworzy nazwę w polu uproszczonej serii)
    # Paginacja
