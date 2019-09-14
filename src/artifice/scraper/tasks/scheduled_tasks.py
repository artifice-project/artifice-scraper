from artifice.scraper.tasks.base import celery_app

@celery_app.task(name='tasks.scheduled_tasks')
def scheduled_tasks():
    print('Heartbeat')


# @celery_app.task(name='tasks.holding_tank')
# def holding_tank(url, *args, **kwargs):
#     print('Thank you, come again')
#     return 'This is returned from the task'
