from flask import current_app
from artifice.scraper.core.app import create_celery_app

celery_app = create_celery_app()


def run_celery():
    """
    Starts the async task queue
    """
    celery_app.worker_main(['', '-B'])

    # celery_app.start(argv=[
    #         'celery',
    #         'worker',
    #         '--concurrency={}'.format(current_app.config.get('CELERY_WORKERS')),
    #         '--loglevel', current_app.config.get('CELERY_LOG_LEVEL'),
    #         '--logfile', current_app.config.get('CELERY_LOG_FILE')
    #     ]
    # )
