from artifice.scraper.core.app import create_celery_app

celery_app = create_celery_app()

def run_celery():
    """
    Starts the async task queue
    """
    celery_app.worker_main(['', '-B'])
