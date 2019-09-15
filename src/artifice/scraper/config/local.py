from datetime import timedelta
from artifice.scraper.config.constants import *

ENV = 'development'
DEBUG = True
PORT = 5000
LOG_LEVEL = 'DEBUG'
AUTH_TOKEN = 'correcthorsebatterystaple'
JSONIFY_PRETTYPRINT_REGULAR = True
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/artifice_scraper'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_ECHO = True
CELERY_BROKER_URL = 'sqla+postgresql://localhost/artifice_scraper'
CELERY_BACKEND = 'rpc://'
CELERY_WORKERS = 3
CELERY_LOG_LEVEL = 'INFO'
CELERY_INCLUDE = ['artifice.scraper.tasks']
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERYBEAT_SCHEDULE = {
    'scheduled_tasks': {
        'task': 'tasks.scheduled_task',
        'schedule': timedelta(seconds=10),
        'args': ()
    },
}
URL_FOR_STATUS = 'http://{0}:{1}/status'.format(HOST, PORT)
URL_FOR_QUEUE = 'http://{0}:{1}/queue'.format(HOST, PORT)
URL_FOR_CONTENT = 'http://{0}:{1}/content'.format(HOST, PORT)

ERROR_404_HELP = False
