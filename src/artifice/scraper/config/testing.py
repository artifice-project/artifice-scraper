from artifice.scraper.config.constants import *

ENV = 'testing'
DEBUG = True
TESTING = True
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/artifice_scraper_test'
SQLALCHEMY_TRACK_MODIFICATIONS = False
CELERY_BROKER_URL = 'redis://@localhost'
CELERY_INCLUDE = ['artifice.scraper.tasks']
CELERY_BACKEND = 'rpc://'
ERROR_404_HELP = False
