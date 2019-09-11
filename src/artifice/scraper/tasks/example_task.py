from .base import celery

@celery.task(name='tasks.example_task')
def example_task():
    print('Hello celery!')
