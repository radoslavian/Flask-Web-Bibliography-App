'''
Configurations options for different deployments.
Based on solutions from:
Grinberg, Miguel. Flask Web Development. Beijing [etc.], 2018.
'''

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    APP_ADMIN = os.environ.get('APP_ADMIN')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX = '[Bibliography App]'
    MAIL_SENDER = 'Admin <bibapp@example.com>'
    LIST_ENTRIES_PER_PAGE = 20
    SHORT_LIST_ENTRIES_PER_PAGE = 5
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL') or 'http://localhost:9200/'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SERVER_NAME = 'localhost.localdomain:5000'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    LIST_ENTRIES_PER_PAGE = 10
    # os.environ.get('TEST_DATABASE_URL') or \


class TestingMysqlConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_DATABASE_URL')


class ProductionConfig(Config):
    "Production config for MySQL server."
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_DATABASE_URL')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'testing_mysql' : TestingMysqlConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
