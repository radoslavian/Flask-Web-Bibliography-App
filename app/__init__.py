'''Application package constructor module.
'''

from flask import Flask
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch
from flask_login import LoginManager
from config import config
from flask_breadcrumbs import Breadcrumbs

bootstrap = Bootstrap()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
mail = Mail()


def create_app(config_name='development'):
    '''Application factory function.

    Based on solutions from:
    Grinberg, Miguel. Flask Web Development. Beijing [etc.], 2018.
    '''

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    Breadcrumbs(app=app)
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None

    if 'sqlite' in app.config['SQLALCHEMY_DATABASE_URI']:
        def _fk_pragma_on_connect(dbapi_con, con_record):
            '''Turns on ForeignKey constraint on each connection
            when using SQLite.
            https://gist.github.com/asyd/a7aadcf07a66035ac15d284aef10d458
            '''
            dbapi_con.execute('pragma foreign_keys=ON')

        with app.app_context():
            from sqlalchemy import event
            event.listen(db.engine, 'connect', _fk_pragma_on_connect)

    return app
