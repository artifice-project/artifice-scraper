import os
from datetime import timedelta
from artifice.scraper.utils import number_of_cores
from artifice.scraper.config.constants import *

ENV = 'production'
DEBUG = False
LOG_LEVEL = 'INFO'
LOG_FILE = 'flask.log'
AUTH_TOKEN = os.environ['AUTH_TOKEN']
JSONIFY_PRETTYPRINT_REGULAR = True
SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
SQLALCHEMY_TRACK_MODIFICATIONS = False
CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
CELERY_BACKEND = 'rpc://'
CELERY_WORKERS = number_of_cores()
CELERY_LOG_FILE = 'celery.log'
CELERY_LOG_LEVEL = 'INFO'
CELERY_INCLUDE = ['artifice.scraper.tasks']
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERYBEAT_SCHEDULE = {
    'scheduled_tasks': {
        'task': 'tasks.scheduled_task',
        'schedule': timedelta(minutes=2),
        'args': ()
    },
}
URL_FOR_STATUS = 'http://{0}/status'.format(HOST)
URL_FOR_QUEUE = 'http://{0}/queue'.format(HOST)
URL_FOR_CONTENT = 'http://{0}/content'.format(HOST)

ERROR_404_HELP = False
