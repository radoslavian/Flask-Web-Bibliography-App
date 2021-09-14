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

    def test_documents_selfref_relations(self):
        master_doc = Document(
            title_proper='Fantastyka',
            other_title_inf='[miesięcznik literatury SF / '
            + 'Adam Hollanek red. nacz.]',
            edition_statement='Krajowe Wydawnictwo Czasopism RSW'
            + '"Prasa-Książka-Ruch" 1982, 1-1990, 6 = 93 (czerw.).',
            publication_date='1982-1990',
            issn='0209-1631')

        title_1 = 'Magiczne zwierciadła baśni i fantasy'
        title_2 = 'Trudna droga do miasta'
        dependent_doc_1 = Document(
            title_proper=title_1)
        dependent_doc_2 = Document(
            title_proper=title_2)

        for dependent_doc in (dependent_doc_1, dependent_doc_2):
            master_doc.dependent_docs.append(RelatedDocuments(
                dependent_doc=dependent_doc,
                description='Article'))
            db.session.add(dependent_doc)

        db.session.add_all([master_doc])
        db.session.commit()

        master = Document.query.filter_by(title_proper='Fantastyka').first()
        self.assertEqual(master.title_proper, 'Fantastyka')
        self.assertTrue(master.dependent_docs[0].dependent_doc.title_proper in
                        (title_1, title_2))

        dependent = Document.query.filter_by(
            title_proper=title_1).first()
        self.assertEqual(dependent.master_document[0].master_doc.title_proper,
                         'Fantastyka')
        self.assertFalse(dependent.dependent_docs)
