import os
from datetime import timedelta
from artifice.scraper.utils import number_of_cores
from artifice.scraper.config.constants import *

ENV = 'production'
DEBUG = False
LOG_LEVEL = 'INFO'
HOST = 'http://127.0.0.1'
LOG_FILE = '/home/ubuntu/log/flask/flask.log'
LOG_FILE = os.environ['LOG_FILE']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
JSONIFY_PRETTYPRINT_REGULAR = True
SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
SQLALCHEMY_TRACK_MODIFICATIONS = False
CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
CELERY_BACKEND = 'rpc://'
CELERY_WORKERS = number_of_cores()
CELERY_LOG_FILE = '/var/log/celery/celery.log' # think this is overridden..
CELERY_LOG_LEVEL = 'INFO'                       # same here
CELERY_INCLUDE = ['artifice.scraper.tasks']
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERYBEAT_SCHEDULE = {
    'scheduled_tasks': {
        'task': 'tasks.scheduled_task',
        'schedule': timedelta(minutes=2),
        'args': ()
    },
    'scheduled_tasks1': {
        'task': 'tasks.health_check',
        'schedule': timedelta(seconds=30),
        'args': ()
    },
}
URL_FOR_STATUS = '{0}/status'.format(HOST)
URL_FOR_QUEUE = '{0}/queue'.format(HOST)
URL_FOR_CONTENT = '{0}/content'.format(HOST)

ERROR_404_HELP = False
