import unittest
from flask import current_app
from app import create_app, db
from app.models import *
from app import fake, queries
import re


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        DocumentType.add_basic_document_types()
        ResponsibilityName.add_basic_responsibilities()

        # setting up testing client:
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def count_person_names(self, max_iteration_count=2000):
        '''Counts entries (names and name variants) from
        the browse_people() /browse/people/ route (values for
        every page).
        '''
        while True:
            if page_num > max_iteration_count:
                raise ValueError(f'max_iteration_count '
                                 '({max_iteration_count} exceeded.')

            response = self.client.get(f'/browse/people/?page={page_num}')
            if response.status_code != 200:
                break
            response_text = response.get_data(as_text=True)
            people_names_number += len(re.findall(
                'href="/browse/people/id', response_text))
            name_variants_number += len(re.findall(
                'href="/browse/people/name-variants/', response_text))
            page_num += 1

        return people_names_number + name_variants_number

    # pomyśleć o lepszych nazwach metod i klas
    class Counter:
        '''Helper abstract class for testing /browse/people/
        route.
        '''
        def __init__(self, client):
            self.client = client
            self.page_num = 1
            self.response = None
            self.return_value = 0

        def custom_count(self):
            pass

        def main_loop(self, max_iteration_count=2000):
            while True:
                self.response = self.client.get(
                f'/browse/people/?page={self.page_num}')
                self.response_text = self.response.get_data(as_text=True)
                if self.page_num > max_iteration_count:
                    raise ValueError(f'max_iteration_count '
                                 '({max_iteration_count} exceeded.')
                if self.response.status_code != 200:
                    break
                self.custom_fn()
                self.page_num += 1
            return self.return_value

        def __repr__(self):
            return f'<{self.return_value}>'

    class PersonNames(Counter):
        def custom_fn(self):
            self.return_value += len(re.findall(
                'href="/browse/people/id', self.response_text))
            self.return_value += len(re.findall(
                'href="/browse/people/name-variants/', self.response_text))

    class NamesVariantsList(Counter):
        def __init__(self, client):
            TestApp.Counter.__init__(self, client)
            self.return_value = []

        def custom_fn(self):
            self.return_value.extend(re.findall(
                r'href="/browse/people/id.*"', self.response_text))
            self.return_value.extend(re.findall(
                r'href="/browse/people/name-variants/id.*',
                self.response_text))


    def test_person_name_list(self):
        '''Test for basic (with no additional parameters)
        /browse/people/ route.
        '''
        Role.insert_roles()
        DocumentType.add_basic_document_types()
        ResponsibilityName.add_basic_responsibilities()
        fake.people(30)
        fake.geographic_locations(10)
        fake.collective_bodies(10)
        fake.keywords(10)
        Language.add_languages(10)
        fake.documents(10)

        # check if the route exists:
        response = self.client.get('/browse/people/')
        self.assertEqual(response.status_code, 200)

        # compares number of entries from the query with the one
        # displayed on the list
        names_count_from_query = queries.list_people_name_variants().count()
        self.assertEqual(names_count_from_query,
                         TestApp.PersonNames(self.client).main_loop())

        # check if each item in the list of names and name variants
        # appears only once
        name_and_variant_urls = TestApp.NamesVariantsList(
            client=self.client).main_loop()
        for item in name_and_variant_urls:
            self.assertTrue(name_and_variant_urls.count(item), 1)
