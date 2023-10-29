"""Test creating new/editing existing documents."""

import unittest
from flask import current_app
from app import create_app, db


class TestAddingDoc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # wykonać wg. pdr s 231
        pass

    def test_text_fields(self):
        """Test filling in text fields and adding document into the database.
        """
        pass
