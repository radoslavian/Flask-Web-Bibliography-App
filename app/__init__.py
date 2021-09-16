'''
Application package constructor module.
'''

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    '''Application factory function.

Based on solutions from:
Grinberg, Miguel. Flask Web Development. Beijing [etc.], 2018.
'''

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    # routes, custom error pages etc. will come here

    return app
