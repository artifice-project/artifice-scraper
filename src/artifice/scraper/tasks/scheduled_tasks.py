from artifice.scraper.tasks.base import celery_app


@celery_app.task(name='tasks.scheduled_task')
def scheduled_task():
    print('Heartbeat')
