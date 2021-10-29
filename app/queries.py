from app.models import *
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
