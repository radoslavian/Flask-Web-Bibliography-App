import unittest
from flask import current_app
from app import create_app, db
from app.models import *
from datetime import date


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

        db.session.add_all([master_doc, user])
        db.session.commit()

    def setup_collective_bodies(self):
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

        master_doc = Document.query.filter_by(
            title_proper='Fantastyka').first()
        main_resp = ResponsibilityName(
            responsibility_name='Main responsibility',
            responsibility_abbr='Main')

        assoc = ResponsibilityCollectivity(
            document=master_doc,
            responsibility=main_resp,
            collectivity=collective_body_3)

        master_doc.collectivity_subjects.extend(
            [collective_body_1, collective_body_2])

        db.session.add_all([master_doc, assoc])
        db.session.commit()

    def setup_people_records(self):
        s_lem = Person(
            forenames='Stanisław',
            last_name='Lem',
            note='Pisarz SF',
            life_years='1921-2006')
        j_zajdel = Person(
            forenames='Janusz Andrzej',
            last_name='Zajdel',
            note='Pisarz SF.',
            birth_date=date(1938, 8, 15),
            death_date=date(1985, 7, 19))
        a_hollanek = Person(
            forenames='Adam',
            last_name='Hollanek',
            note='Pisarz i publicysta.',
            life_years='1922-1998')

        db.session.add_all([s_lem, j_zajdel, a_hollanek])

    def setup_topics_people(self):
        fantastyka = Document.query.filter_by(
            title_proper='Fantastyka').first()
        article = Document.query.filter_by(
            title_proper='Trudna droga do miasta').first()
        s_lem = Person.query.filter_by(last_name='Lem').first()
        j_zajdel = Person.query.filter_by(last_name='Zajdel').first()

        article.topic_people.append(j_zajdel)
        fantastyka.topic_people.extend([s_lem, j_zajdel])

        db.session.add_all([article, fantastyka])
        db.session.commit()

    def setup_responsibilities(self):
        editor_in_chief = ResponsibilityName(
            responsibility_name='Editor in chief')
        author = ResponsibilityName(
            responsibility_name='Author')

        db.session.add_all([editor_in_chief, author])

    def setup_geo_locations(self):
        cracow = GeographicLocation(
            name='Cracow',
            native_name='Kraków',
            note='City in Poland.')
        georgia = GeographicLocation(
            name='Georgia',
            native_name='საქართველო',
            other_name='Sakartvelo',
            note='Country in the caucasus.')
        new_york = GeographicLocation(
            name='New York',
            other_name='Nowy Jork',
            note='City in the US (in the New York State).')

        db.session.add_all([cracow, georgia, new_york])
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

    def test_document_types(self):
        doc_type_periodical = DocumentType(
            name='Periodical',
            description='A type for periodicals.')
        doc_type_periodical_single_issue = DocumentType(
            name='Article',
            description='An article from a periodical.')

        document = Document.query.filter_by(title_proper='Fantastyka').first()
        document.document_type = doc_type_periodical

        db.session.add_all(
            [document, doc_type_periodical_single_issue])
        db.session.commit()

        self.assertEqual(
            DocumentType.query.filter_by(
                name='Article').first().description,
            'An article from a periodical.')
        self.assertEqual(
            DocumentType.query.filter_by(name='Periodical'). \
            first().documents[0].title_proper,
            'Fantastyka')

    def test_related_documents(self):
        master = Document.query.filter_by(title_proper='Fantastyka').first()
        self.assertEqual(master.title_proper, 'Fantastyka')
        self.assertTrue(master.dependent_docs[0].dependent_doc.title_proper in
                        (self.title_1, self.title_2))

        dependent = Document.query.filter_by(
            title_proper=self.title_1).first()
        self.assertEqual(dependent.master_document.master_doc.title_proper,
                         'Fantastyka')
        self.assertFalse(dependent.dependent_docs)

        master.dependent_docs = []
        db.session.add(master)
        db.session.commit()

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
        self.setup_collective_bodies()
        document_1 = Document.query.filter_by(
            title_proper='Fantastyka').first()
        subjects = document_1.collectivity_subjects.all()

        self.assertEqual(len(subjects), 2)
        self.assertNotEqual(subjects[0], subjects[1])

        # removing relationship from a join table in a many-to-many
        # relationship - two ways:
        # sbj = subjects.pop()
        # document_1.collectivity_subjects = subjects
        document_1.collectivity_subjects.remove(subjects[0])
        db.session.add(document_1)
        db.session.commit()

        self.assertEqual(
            document_1.collectivity_subjects.count(), 1)

    def test_collectivity_responsibilities(self):
        self.setup_collective_bodies()
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

        main_doc.responsibility_collectivities = []
        db.session.add(main_doc)
        db.session.commit()

    def test_document_languages(self):
        polish = Language(
            language_name='Polish',
            native_name='język polski',
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

        self.assertEqual(doc.language.language_name, 'Polish')
        self.assertEqual(chinese.documents_original_lang.count(), 2)

    def test_subject_keywords(self):
        keyword_1 = Keyword(keyword='Fantastyka naukowa')
        keyword_2 = Keyword(keyword='Literatura fantasy')
        keyword_3 = Keyword(keyword='Warsaw',
                            determiner='IND, USA')

        fantastyka = Document.query.filter_by(
            title_proper='Fantastyka').first()
        article_1 = Document.query.filter_by(
            title_proper='Trudna droga do miasta').first()
        article_2 = Document.query.filter_by(
            title_proper='Magiczne zwierciadła baśni i fantasy').first()

        fantastyka.keywords.extend([keyword_1, keyword_2])
        article_1.keywords.extend([keyword_2, keyword_3])
        article_2.keywords.append(keyword_3)

        db.session.add_all([fantastyka, article_1, article_2])
        db.session.commit()

        from sqlalchemy.exc import IntegrityError

        def check_UniqueConstraint(keywords):
            try:
                fantastyka.keywords.extend(keywords)
                db.session.add(fantastyka)
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                raise

        for keywords in ([keyword_2],
                         [keyword_1, keyword_2],
                         [keyword_1, keyword_3]):
            self.assertRaises(
                IntegrityError,
                lambda: check_UniqueConstraint(keywords))

        fantastyka_keywords = tuple(
            keyword in fantastyka.keywords
            for keyword in [keyword_1, keyword_2])

        self.assertEqual(fantastyka.keywords.count(), 2)
        self.assertTrue(all(fantastyka_keywords))
        self.assertFalse(keyword_3 in fantastyka.keywords)
        self.assertEqual(keyword_1.documents.count(), 1)
        self.assertEqual(keyword_1.documents[0].title_proper, 'Fantastyka')

    def test_topic_people(self):
        self.setup_people_records()
        self.setup_topics_people()

        fantastyka = Document.query.filter_by(
            title_proper='Fantastyka').first()
        article = Document.query.filter_by(
            title_proper='Trudna droga do miasta').first()
        j_zajdel = Person.query.filter_by(last_name='Zajdel').first()
        zajdel_topic_documents = [document.title_proper for document in
                                  j_zajdel.documents_topics]

        self.assertEqual(fantastyka.topic_people.count(), 2)
        self.assertEqual(article.topic_people[0].last_name, 'Zajdel')
        self.assertTrue('Trudna droga do miasta' in zajdel_topic_documents)

        article.topic_people = []
        db.session.commit()

    def test_people_responsibilities(self):
        self.setup_responsibilities()
        self.setup_people_records()

        hollanek, zajdel = [Person.query.filter_by(
            last_name=last_name).first()
            for last_name in ('Hollanek', 'Zajdel')]
        editor_resp, author_resp = [ResponsibilityName.query.filter_by(
            responsibility_name=responsibility).first()
            for responsibility in ('Editor in chief', 'Author')]
        fantastyka, article = [Document.query.filter_by(
            title_proper=title).first()
            for title in ('Fantastyka',
                          'Magiczne zwierciadła baśni i fantasy')]

        fantastyka_editor = ResponsibilityPerson(
            responsibility=editor_resp,
            person=hollanek,
            document=fantastyka)
        article_author = ResponsibilityPerson(
            responsibility=author_resp,
            person=zajdel,
            document=article)

        db.session.add_all([fantastyka_editor, article_author])
        db.session.commit()

        self.assertEqual(fantastyka.responsibilities_people[0]. \
                         person.last_name, 'Hollanek')
        self.assertEqual(fantastyka.responsibilities_people[0]. \
                         responsibility. responsibility_name,
                         'Editor in chief')
        self.assertEqual(
            zajdel.responsibilities[0].document.title_proper,
            'Magiczne zwierciadła baśni i fantasy')
        self.assertEqual(zajdel.responsibilities[0]. \
                         responsibility.responsibility_name, 'Author')

        fantastyka.responsibilities_people = [] 
        db.session.commit()

    def test_subjects_geography(self):
        self.setup_geo_locations()

        cracow = GeographicLocation.query.filter_by(
            native_name='Kraków').first()
        georgia = GeographicLocation.query.filter_by(
            name='Georgia').first()

        document_1 = Document.query.filter_by(
            title_proper='Magiczne zwierciadła baśni i fantasy').first()
        document_2 = Document.query.filter_by(
            title_proper='Trudna droga do miasta').first()

        self.assertTrue(all([document_1, document_2]))

        document_1.subjects_locations.append(cracow)
        document_2.subjects_locations.extend([cracow, georgia])

        db.session.add_all([document_1, document_2])
        db.session.commit()

        self.assertEqual(
            document_2.subjects_locations[1].name, 'Georgia')
        self.assertEqual(cracow.documents_topics.count(), 2)
        self.assertEqual(
            cracow.documents_topics[0].title_proper,
            'Magiczne zwierciadła baśni i fantasy')

        document_2.subjects_locations = []
        db.session.add(document_2)
        db.session.commit()

    def test_publication_places(self):
        self.setup_geo_locations()

        fantastyka = Document.query.filter_by(
            title_proper='Fantastyka').first()
        cracow = GeographicLocation.query.filter_by(
            native_name='Kraków').first()
        new_york = GeographicLocation.query.filter_by(
            name='New York').first()

        self.assertTrue(all([fantastyka, cracow, new_york]))

        fantastyka.publication_places.extend([cracow, new_york])
        db.session.add(fantastyka)
        db.session.commit()

        publication_places = [place.name
                              for place in fantastyka.publication_places]
        for place in 'Cracow', 'New York':
            self.assertTrue(place in publication_places)

        self.assertEqual(new_york.document_publication_place[0].title_proper,
                         'Fantastyka')
        fantastyka.publication_places = []
        db.session.add(fantastyka)
        db.session.commit()

    def test_person_name_variants(self):
        self.setup_people_records()

        hollanek = Person.query.filter_by(last_name='Hollanek').first()
        name_variant_1 = PersonNameVariant(
            first_name_variant='Dżon',
            last_name_variant='Kołolski')
        name_variant_2 = PersonNameVariant(
            first_name_variant='Jan',
            last_name_variant='Nowak')
        hollanek.name_variants.extend([name_variant_1, name_variant_2])

        db.session.add(hollanek)
        db.session.commit()

        self.assertEqual(hollanek.name_variants.count(), 2)
        last_name_variants = [name.last_name_variant
                              for name in (name_variant_1, name_variant_2)]
        for name in hollanek.name_variants:
            self.assertTrue(name.last_name_variant in last_name_variants)

        hollanek.name_variants = []
        db.session.commit()
