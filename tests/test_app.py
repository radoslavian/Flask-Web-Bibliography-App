import unittest
from flask import current_app
from app import create_app, db
from app.models import *


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.setup_db()

    def setup_db(self):
        user = User(username='tadzik',
                    name='Pan Tadeusz')

        master_doc = Document(
            title_proper='Fantastyka',
            other_title_inf='[miesięcznik literatury SF / '
            + 'Adam Hollanek red. nacz.]',
            edition_statement='Krajowe Wydawnictwo Czasopism RSW'
            + '"Prasa-Książka-Ruch" 1982, 1-1990, 6 = 93 (czerw.).',
            publication_date='1982-1990',
            issn='0209-1631')

        self.title_1 = 'Magiczne zwierciadła baśni i fantasy'
        self.title_2 = 'Trudna droga do miasta'

        dependent_doc_1 = Document(
            title_proper=self.title_1)
        dependent_doc_2 = Document(
            title_proper=self.title_2)

        for dependent_doc in (dependent_doc_1, dependent_doc_2):
            master_doc.dependent_docs.append(RelatedDocuments(
                dependent_doc=dependent_doc,
                description='Article'))

        collective_body_1 = CollectiveBody(
            name='Generalna Dyrekcja Dróg Krajowych i Autostrad',
            address='58-306 Wałbrzych',
            description='''The General Directorate for National Roads and
Motorways is the central authority of national administration set up to 
manage the national roads and implementation of
the state budget in Poland.''')
        collective_body_2 = CollectiveBody(
            name='Narodowy Fundusz Zdrowia',
            description='''The Narodowy Fundusz Zdrowia is
the National Health Fund of Poland. ''',
            address='The Colosseum Building, Warsaw, Poland')
        collective_body_3 = CollectiveBody(
            name='Zakład Narodowy im Ossolińskich',
            description='''The Ossolineum or the National
Ossoliński Institute is a Polish cultural foundation''',
            address='ul. Szewska 37, 50-139 Wrocław')

        main_resp = ResponsibilityName(
            responsibility_name='Main responsibility',
            responsibility_abbr='Main')

        assoc = ResponsibilityCollectivity(
            document=master_doc,
            responsibility=main_resp,
            collectivity=collective_body_3)

        master_doc.collectivity_subjects.extend(
            [collective_body_1, collective_body_2])

        db.session.add_all([master_doc, user, assoc])
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(self.app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_db_admin_role(self):
        admin = Role(name='admin')
        db.session.add(admin)
        db.session.commit()

        self.assertTrue(Role.query.first() is admin)

    # test dokumentu:
    # - relacje:
    # -- typ dokumenty
    # -- język
    # -- język oryginału
    # - tytuł i pozostałe pola

    def test_document_types(self):
        doc_type_periodical = DocumentType(
            name='Periodical',
            description='A type for periodicals.')
        doc_type_periodical_single_issue = DocumentType(
            name='Article',
            description='A single issue of a periodical.')

        db.session.add_all([doc_type_periodical,
                            doc_type_periodical_single_issue])
        db.session.commit()

        self.assertEqual(
            DocumentType.query.filter_by(
                name='Periodical').first().description,
            'A type for periodicals.')

    def test_related_documents(self):
        master = Document.query.filter_by(title_proper='Fantastyka').first()
        self.assertEqual(master.title_proper, 'Fantastyka')
        self.assertTrue(master.dependent_docs[0].dependent_doc.title_proper in
                        (self.title_1, self.title_2))

        dependent = Document.query.filter_by(
            title_proper=self.title_1).first()
        self.assertEqual(dependent.master_document[0].master_doc.title_proper,
                         'Fantastyka')
        self.assertFalse(dependent.dependent_docs)

    def test_record_locking(self):
        record = Document.query.filter_by(title_proper='Fantastyka').first()
        user = User.query.first()

        record.lock(user)
        self.assertTrue(record.locked)
        self.assertRegex(
            str(record.lock_timestamp), r'\d+-\d+-\d+\s\d+:\d+:\d+\.\d+')

        record.unlock()
        self.assertFalse(record.locked)

    def test_collectivity_subjects(self):
        document_1 = Document.query.filter_by(
            title_proper='Fantastyka').first()
        subjects = document_1.collectivity_subjects.all()

        self.assertEqual(len(subjects), 2)
        self.assertNotEqual(subjects[0], subjects[1])

    def test_collectivity_responsibility(self):
        main_doc = Document.query.filter_by(title_proper='Fantastyka').first()

        self.assertEqual(
            main_doc.responsibility_collectivities[0]. \
            responsibility.responsibility_name, 'Main responsibility')
        self.assertEqual(
            main_doc.responsibility_collectivities[0].collectivity.name,
            'Zakład Narodowy im Ossolińskich')

        collective_body = CollectiveBody.query.filter_by(
            name='Zakład Narodowy im Ossolińskich').first()
        self.assertEqual(collective_body.responsibility_collectivities[0]. \
                         document.title_proper, 'Fantastyka')

    def test_languages(self):
        polish = Language(
            language_name='Polish',
            native_name='polski',
            iso_639_1_language_code='pl',
            iso_639_2_language_code='pol',
            other_name='Polnisch (ger.)')
        chinese = Language(
            language_name='Chinese',
            native_name='中国人',
            iso_639_1_language_code='zh',
            iso_639_2_language_code='chi',
            other_name='Chinesisch (ger.)')

        doc = Document.query.filter_by(title_proper='Fantastyka').first()
        doc.language = polish
        doc.original_language = chinese

        doc_2 = Document.query.filter_by(
            title_proper='Magiczne zwierciadła baśni i fantasy').first()
        doc_2.original_language = chinese

        db.session.add_all([doc, doc_2])
        db.session.commit()

        chinese
        self.assertEqual(doc.language.language_name, 'Polish')
        self.assertEqual(len(chinese.documents_original_lang), 2)
