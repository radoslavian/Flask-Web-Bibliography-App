import unittest
from app import models

# właściwe testowanie:
# konfiguracja do testów
# test na bd w pamięci (sqlite/memory)

class RolesTestCase(unittest.TestCase):
    def setUp(self):
        models.db.create_all()
        self.admin = models.Role(name='admin')
        models.db.session.add(self.admin)
        models.db.session.commit()

    def test_roles(self):
        self.assertTrue(models.Role.query.all()[0] is self.admin)
