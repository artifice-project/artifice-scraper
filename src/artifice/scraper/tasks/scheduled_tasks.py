from artifice.scraper.tasks.base import celery_app


@celery_app.task(name='tasks.scheduled_task')
def scheduled_task():
    from flask import current_app
    env = current_app.config.get('ENV', '<missing>')
    print(' * Heartbeat (config:{0})'.format(env))
