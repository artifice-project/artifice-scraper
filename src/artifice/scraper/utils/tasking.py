def send_to_celery(*args, **kwargs):
    from artifice.scraper.tasks.callable_tasks import holding_tank as task
    r = task.delay(*args, **kwargs)
    return r
