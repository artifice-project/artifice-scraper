import os
from datetime import timedelta
from artifice.scraper.config.constants import *

ENV = 'production'
DEBUG = False
# LOG_LEVEL = 'INFO'
JSONIFY_PRETTYPRINT_REGULAR = True
SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
SQLALCHEMY_TRACK_MODIFICATIONS = False
CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
CELERY_INCLUDE = ['artifice.scraper.tasks']
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERYBEAT_SCHEDULE = {
    'example_task': {
        'task': 'tasks.example_task',
        'schedule': timedelta(minutes=2),
        'args': ()
    },
}

ERROR_404_HELP = False
