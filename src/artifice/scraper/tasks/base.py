from flask import current_app
from artifice.scraper.core.app import create_celery_app

celery_app = create_celery_app()


def run_celery(*args):
    """
    Starts the async task queue
    """
    if current_app.config.get('ENV') == 'production':
        args = [
            '--logfile',
            current_app.config['CELERY_LOG_FILE'],
            '-E',
        ]
    celery_app.worker_main(
        [
            '',
            '-B',
            '--loglevel',
            current_app.config['CELERY_LOG_LEVEL'],
            '--concurrency={0}'.format(
                current_app.config['CELERY_WORKERS']),
            *args,
        ]
    )
