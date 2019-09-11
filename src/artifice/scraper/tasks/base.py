from artifice.scraper.core.app import create_celery_app

celery = create_celery_app()

def run_celery():
    celery.worker_main(['', '-B'])
