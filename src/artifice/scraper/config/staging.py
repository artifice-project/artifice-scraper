import os
from datetime import timedelta

# DEBUG = True
ENV = 'production'
SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
SQLALCHEMY_TRACK_MODIFICATIONS = False
CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
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
