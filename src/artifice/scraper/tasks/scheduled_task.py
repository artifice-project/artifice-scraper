from artifice.scraper.tasks.base import celery_app

@celery_app.task(name='tasks.scheduled_task')
def scheduled_task():
    print('Hello celery!')


@celery_app.task(name='tasks.callable_task')
def callable_task():
    print('Thank you, come again')
