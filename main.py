import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.cli.command()
def test():
    '''Run the unit tests.
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    # tests = unittest.TestLoader().discover('tests', pattern='*view*')
    unittest.TextTestRunner(verbosity=2).run(tests)
