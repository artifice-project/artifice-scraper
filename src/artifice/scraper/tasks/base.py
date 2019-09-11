from artifice.scraper.core.app import create_celery_app

celery = create_celery_app()

def run_celery():
    """
    Starts the async task queue
    """
    celery.worker_main(['', '-B'])
