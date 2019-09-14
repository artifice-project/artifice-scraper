from .base import celery_app

@celery_app.task(name='tasks.callable_task')
def callable_task():
    print('Callable Celery entrypoint')
