from artifice.scraper.tasks.base import celery_app

@celery_app.task(name='tasks.example_task')
def example_task():
    print('Hello celery!')
