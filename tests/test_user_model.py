'''Authentication tests.
Test cases based on: M. Grinberg...'''

import unittest
from app.models import User, AnonymousUser, Role, Permissions
from app import create_app, db

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        u = User(password='Cici')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='Cici')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='Cici')
        self.assertTrue(u.verify_password('Cici'))
        self.assertFalse(u.verify_password('Bakufu'))

    def test_password_salts_are_random(self):
        u = User(password='kot')
        u2 = User(password='kot')
        self.assertTrue(u.password_hash != u2.password_hash)

    def test_admin_role(self):
        admin = Role(name='admin')
        db.session.add(admin)
        db.session.commit()

        self.assertTrue(Role.query.filter_by(name='admin').first() is admin)

    def test_user_role(self):
        u = User(email='user@example.com', password='Cici')
        self.assertTrue(u.can(Permissions.SAVE_TO_LIST))
        self.assertFalse(u.can(Permissions.EDIT_BIBLIOGRAPHY))
        self.assertFalse(u.can(Permissions.ADMIN))

    def test_anonymous_user(self):
        u = AnonymousUser()
        for permission in [getattr(Permissions, perm_name) for perm_name in
                           ('SAVE_TO_LIST', 'EDIT_BIBLIOGRAPHY', 'ADMIN')]:
            self.assertFalse(u.can(permission))
