from datetime import timedelta
from artifice.scraper.config.constants import *

ENV = 'development'
DEBUG = True
PORT = 5000
HOST = 'http://127.0.0.1:{0}'.format(PORT)
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
    # 'scheduled_tasks1': {
    #     'task': 'tasks.health_check',
    #     'schedule': timedelta(seconds=20),
    #     'args': ()
    # },
}
URL_FOR_STATUS = '{0}/status'.format(HOST)
URL_FOR_QUEUE = '{0}/queue'.format(HOST)
URL_FOR_CONTENT = '{0}/content'.format(HOST)

ERROR_404_HELP = False
