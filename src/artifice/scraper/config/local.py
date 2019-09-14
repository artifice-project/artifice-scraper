from datetime import timedelta
from artifice.scraper.config.constants import *

ENV = 'development'
DEBUG = True
# LOG_LEVEL = 'DEBUG'
JSONIFY_PRETTYPRINT_REGULAR = True
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/artifice_scraper'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_ECHO = True
CELERY_BROKER_URL = 'sqla+postgresql://localhost/artifice_scraper'
CELERY_BACKEND = 'rpc://'
CELERY_WORKERS = 8
CELERY_LOG_FILE = '-'
CELERY_LOG_LEVEL = 'DEBUG'
CELERY_INCLUDE = ['artifice.scraper.tasks']
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERYBEAT_SCHEDULE = {
    'scheduled_task': {
        'task': 'tasks.scheduled_task',
        'schedule': timedelta(seconds=10),
        'args': ()
    },
}

ERROR_404_HELP = False
