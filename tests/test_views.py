import unittest
from flask import current_app, url_for
from app import create_app, db
from app import fake
from app.utils import queries
from app.main.views import *
from app.models import *
from sqlalchemy.sql.expression import func
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

    def check_response(self, endpoint, response_code, **kwargs):
        '''Helper for checking http responses for a given route.
        '''
        response = self.client.get(url_for(endpoint, **kwargs))
        self.assertEqual(response.status_code, response_code)

    # pomyśleć o lepszych nazwach metod i klas
    class Counter:
        '''Helper abstract class for testing routes.
        '''
        def __init__(self, client, endpoint):
            self.client = client
            self.page_num = 1
            self.response = None
            self.return_value = 0
            self.endpoint = endpoint

        def custom_fn(self):
            pass

        def main_loop(self, max_iteration_count=500):
            while True:
                self.response = self.client.get(
                    url_for(self.endpoint, page=self.page_num))
                self.response_text = self.response.get_data(as_text=True)
                if self.page_num > max_iteration_count:
                    raise RuntimeError('max_iteration_count '
                                       f'({max_iteration_count}) exceeded.')
                if self.response.status_code != 200:
                    break
                self.custom_fn()
                self.page_num += 1
            return self.return_value

        def __repr__(self):
            return f'Endpoint {self.endpoint}: {self.return_value}'

    class PersonNames(Counter):
        def custom_fn(self):
            self.return_value += len(re.findall(
                'href="/browse/people/id', self.response_text))
            self.return_value += len(re.findall(
                'href="/browse/people/name-variants/', self.response_text))

    class NamesVariantsList(Counter):
        def __init__(self, client, *pargs, **kwargs):
            TestApp.Counter.__init__(self, client, *pargs, **kwargs)
            self.return_value = []

        def custom_fn(self):
            self.return_value.extend(re.findall(
                r'href="/browse/people/id.*"', self.response_text))
            self.return_value.extend(re.findall(
                r'href="/browse/people/name-variants/id.*',
                self.response_text))

    def test_personal_names_list(self):
        COUNT = 30
        fake.people(COUNT)

        # check if the route exists:
        self.check_response('main.browse_people', 200)

        # check 404 response:
        self.check_response('main.browse_people', 404, page=int(COUNT/3))

        # compares number of entries from the query with the one
        # displayed on the list
        names_count_from_query = queries.list_people_name_variants().count()
        self.assertEqual(names_count_from_query,
                         TestApp.PersonNames(
                             self.client, 'main.browse_people').main_loop())

        # check if each item from the list of names and name variants
        # appears only once
        name_and_variant_urls = TestApp.NamesVariantsList(
            client=self.client, endpoint='main.browse_people').main_loop()
        for item in name_and_variant_urls:
            self.assertTrue(name_and_variant_urls.count(item), 1)

    class CollectiveBodyCount(Counter):
        def __init__(self, *pargs, **kwargs):
            TestApp.Counter.__init__(self, *pargs, **kwargs)

            # draws single collective body
            # checks if it's name appears on a list - exactly once
            self.collective_body_name = CollectiveBody.query.order_by(
                func.random()).first().name

        def custom_fn(self):
            self.return_value += len(re.findall(
                self.collective_body_name, self.response_text))

    class GeneralCounter(Counter):
        def __init__(self, search_term, *pargs, **kwargs):
            TestApp.Counter.__init__(self, *pargs, **kwargs)

            # regexp
            self.search_term = search_term

        def custom_fn(self):
            self.return_value += len(re.findall(
                self.search_term, self.response_text))

    def test_collective_names_list(self):
        COUNT = 50
        fake.collective_bodies(COUNT)

        self.check_response('main.collective_bodies_list', 200)

        # 404 response
        self.check_response('main.collective_bodies_list', 404,
                            page=int(COUNT/3))

        self.assertEqual(TestApp.CollectiveBodyCount(
            endpoint='main.collective_bodies_list',
            client=self.client).main_loop(), 1)

    def test_document_types_list(self):
        self.check_response('main.document_types_list', 200)

    class DocumentCount(Counter):
        def __init__(self, *pargs, **kwargs):
            TestApp.Counter.__init__(self, *pargs, **kwargs)

            self.document_title_proper = Document.query.order_by(
                func.random()).first().title_proper

        def custom_fn(self):
            self.return_value += len(re.findall(
                self.document_title_proper, self.response_text))

    def test_documents_list(self):
        Language.add_languages(10)
        fake.people(15)
        fake.geographic_locations(15)
        fake.collective_bodies(15)
        fake.keywords(10)

        DOC_COUNT = 50
        fake.documents(DOC_COUNT)

        self.check_response('main.documents_list', 200)
        self.check_response('main.documents_list', 404,
                            page=int(DOC_COUNT/5))

        self.assertEqual(TestApp.DocumentCount(
            endpoint='main.documents_list',
            client=self.client).main_loop(), 1)

    class GeographicLocationCount(Counter):
        def __init__(self, *pargs, **kwargs):
            TestApp.Counter.__init__(self, *pargs, **kwargs)

            self.name = GeographicLocation.query.order_by(
                func.random()).first().name

        def custom_fn(self):
            self.return_value += len(re.findall(
                self.name, self.response_text))

    def test_geographic_locations_list(self):
        COUNT = 10
        fake.geographic_locations(COUNT)

        self.check_response('main.geographic_locations_list', 200)
        self.check_response('main.geographic_locations_list', 404,
                            page=int(COUNT/3))

        self.assertEqual(TestApp.GeographicLocationCount(
            endpoint='main.geographic_locations_list',
            client=self.client).main_loop(), 1)

    class KeywordCount(Counter):
        def __init__(self, *pargs, **kwargs):
            TestApp.Counter.__init__(self, *pargs, **kwargs)

            self.keyword = Keyword.query.order_by(
                func.random()).first().keyword

        def custom_fn(self):
            self.return_value += len(re.findall(
                self.keyword, self.response_text))

    def test_subject_keywords_list(self):
        COUNT = 10
        fake.keywords(10)

        self.check_response('main.keywords_list', 200)
        self.check_response('main.keywords_list', 404,
                            page=int(COUNT/3))
        self.assertEqual(TestApp.KeywordCount(
            endpoint='main.keywords_list',
            client=self.client).main_loop(), 1)

    class LanguageCount(Counter):
        def __init__(self, *pargs, **kwargs):
            TestApp.Counter.__init__(self, *pargs, **kwargs)

            self.language_name = Language.query.order_by(
                func.random()).first().language_name

        def custom_fn(self):
            self.return_value += len(re.findall(
                f'''>
     {self.language_name}
  </a>''', self.response_text))

    def test_languages_list(self):
        COUNT = 10
        Language.add_languages(COUNT)

        self.check_response('main.language_list', 200)
        self.check_response('main.language_list', 404,
                            page=int(COUNT/2))

        self.assertEqual(TestApp.LanguageCount(
            endpoint='main.language_list',
            client=self.client).main_loop(), 1)

    def single_occurence(self, endpoint, regexp):
        '''Checks if item appears only once on a non-paginated list.
        '''
        self.assertEqual(len(re.findall(
            regexp, self.client.get(url_for(endpoint)
            ).get_data(as_text=True))), 1)

    def test_document_responsibilities_list(self):
        self.check_response('main.responsibilities_list', 200)
        responsibility = ResponsibilityName.query.order_by(
            func.random()).first()
        regexp = (r'"/browse/responsibilities/id.*'
                  f'{responsibility.id}">\n'
                  f'\s+{responsibility.responsibility_name.capitalize()}')
        self.single_occurence('main.responsibilities_list', regexp)

    def test_document_types(self):
        self.check_response('main.document_types_list', 200)
        doc_type = DocumentType.query.order_by(
            func.random()).first()
        regexp = (r'"/browse/document-types/id.*'
                  f'{doc_type.type_id}">\n'
                  f'\s+{doc_type.name.capitalize()}')
        self.single_occurence('main.document_types_list', regexp)

    # tests for entry detail views
    def test_collective_body_details_view(self):
        fake.collective_bodies(6)
        random_coll_body = CollectiveBody.query.order_by(
            func.random()).first()

        self.check_response('main.collective_body_details',
                            200, c_body_id=random_coll_body.id)
        response = self.client.get(url_for(
            'main.collective_body_details', c_body_id=random_coll_body.id))

        # find name of a c.body in a response text:
        self.assertEqual(
            len(re.findall(random_coll_body.name,
                           response.get_data(as_text=True))), 1)

    def test_document_types_details_view(self):
        random_doctype = DocumentType.query.order_by(
            func.random()).first()

        self.check_response('main.document_type',
                            200, type_id=random_doctype.id)
        response = self.client.get(url_for(
            'main.document_type', type_id=random_doctype.id))
        self.assertEqual(len(re.findall(f'<h1>{random_doctype.name}</h1>',
                                        response.get_data(as_text=True))), 1)

    # tests for entry editing routes

    def create_user(self, userdata):
        """Helper for test_logging_in()."""

        Role.insert_roles()
        u = User(**userdata, role=Role.query.filter_by(
            name='Administrator').first())
        db.session.add(u)
        db.session.commit()

    def test_logging_in(self):
        """Check if a user can log into the application."""

        self.create_user({'email': 'jo@example.com',
                          'password': 'kot',
                          'confirmed': True})
        response = self.client.post(
            '/auth/login',
            data={
                'email': 'jo@example.com',
                'password': 'kot',
            })
        self.assertEqual(response.status_code, 302)

    def test_user_view_breadcrumb(self):
        """Test breadcrumb on a user page."""
        self.create_user({'email': 'jo@example.com',
                          'username': 'Joe',
                          'password': 'kot',
                          'confirmed': True})
        self.client.post(
            '/auth/login',
            data={
                'email': 'jo@example.com',
                'password': 'kot',
            })
        response = self.client.get(
            url_for('main.user', username='Joe'))
        response_text = response.get_data(as_text=True)
        self.assertTrue('''<li class=breadcrumb-item>
		
		  <a href="/user-list">
		    User list
		  </a>
		
	      </li>
	      
	    
	      <li class=breadcrumb-item active>
		
		  Joe
		
	      </li>''' in  response_text)
        
