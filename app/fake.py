from random import randint
from datetime import date
from faker import Faker
from . import db
from .models import Person, PersonNameVariant


def people(count=100):
    fake = Faker()
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
        db.session.commit()

        i += 1
