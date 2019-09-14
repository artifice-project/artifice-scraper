def send_to_celery(*args, **kwargs):
    from artifice.scraper.tasks.callable_tasks import callable_task as task
    r = task.delay(*args, **kwargs)
    return r
