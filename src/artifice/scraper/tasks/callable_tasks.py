from .base import celery_app
from .utils import report_done, report_ready
from artifice.scraper.supervisor import Supervisor
from artifice.scraper.parsers import NPRParser


@celery_app.task(name='tasks.holding_tank')
def holding_tank():
    '''
    Entrypoint for the Celery queue. Automatically
    executes functions based on application config.
    '''
    print('Holding Tank')

@celery_app.task(name='tasks.sorting_hat')
def sorting_hat():
    '''
    Responsible for checking whether service is enabled,
    and whether to scrape the URL or return unfinished.
    '''
    print('Sorting Hat')

@celery_app.task(name='tasks.fetch_url')
def fetch_url():
    '''
    Scrapes the URL and passes along the response data
    for content extraction.
    '''
    print('Fetch URL')

@celery_app.task(name='tasks.extract_content')
def extract_content():
    '''
    Determines which parser should be used based on the URL,
    and extracts the content accordingly.
    '''
    print('Extract Content')

@celery_app.task(name='tasks.archive_content')
def archive_content():
    '''
    Stores the extracted content to the database via
    API endpoint.
    '''
    print('Archive Content')

@celery_app.task(name='tasks.archive_url')
def archive_url():
    '''
    Returns the URL to the database via API endpoint,
    status can be either `READY` or `DONE`.
    '''
    print('Archive URL')

@celery_app.task(name='tasks.feed_back')
def feed_back():
    '''
    Automatically add the extracted links from the page
    to the API queue endpoint, perpetuating the process.
    '''
    print('Feed Back')
