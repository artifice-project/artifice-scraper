import time
import requests

from .base import celery_app
from .util import report_done, report_ready
from artifice.scraper.supervisor import Supervisor
from artifice.scraper.parsers import NPRParser


URL_FOR_QUEUE = celery_app._preconf.get('URL_FOR_QUEUE')
URL_FOR_CONTENT = celery_app._preconf.get('URL_FOR_CONTENT')


def auth_header():
    key = 'AUTH_TOKEN'
    token = celery_app._preconf.get(key)
    return {key: token}

def unit_is_under_test():
    key = 'testing'
    is_testing = celery_app._preconf.get(key)
    return is_testing


@celery_app.task(name='tasks.holding_tank')
def holding_tank(url, **kwargs):
    '''
    Entrypoint for the Celery queue. Automatically
    executes functions based on application config.
    '''
    if unit_is_under_test():
        return
    return sorting_hat(url, **kwargs)


@celery_app.task(name='tasks.sorting_hat')
def sorting_hat(url, **kwargs):
    '''
    Responsible for checking whether service is enabled,
    and whether to scrape the URL or return unfinished.
    '''
    status = Supervisor.status()
    if not status['enabled']:
        return archive_url(report_ready(url), **kwargs)
    time.sleep(status['polite'])
    return fetch_url(url, **kwargs)


@celery_app.task(name='tasks.fetch_url')
def fetch_url(url, **kwargs):
    '''
    Scrapes the URL and passes along the response data
    for content extraction.
    '''
    response = requests.get(url)
    return extract_content(response, **kwargs)


@celery_app.task(name='tasks.extract_content')
def extract_content(response, **kwargs):
    '''
    Determines which parser should be used based on the URL,
    and extracts the content accordingly.
    '''
    npr = NPRParser(response)
    content = npr.extract_content()
    return archive_content(content, **kwargs)


@celery_app.task(name='tasks.archive_content')
def archive_content(content, **kwargs):
    '''
    Stores the extracted content to the database via
    API endpoint.
    '''
    response = requests.post(URL_FOR_CONTENT, headers=auth_header(), json=content)
    fb = feed_back(content)
    url = content.get('origin')
    return archive_url(report_done(url), status_code=response.status_code, feedback=fb, **kwargs)


@celery_app.task(name='tasks.archive_url')
def archive_url(json_data, **kwargs):
    '''
    Returns the URL to the database via API endpoint,
    status can be either `READY` or `DONE`.
    '''
    response = requests.put(URL_FOR_QUEUE, headers=auth_header(), json=json_data)
    return response.status_code, {**kwargs}


@celery_app.task(name='tasks.feed_back')
def feed_back(content):
    '''
    Automatically add the extracted links from the page
    to the API queue endpoint, perpetuating the process.
    '''
    json_data = dict(url=content.get('url'))
    response = requests.post(URL_FOR_QUEUE, headers=auth_header(), json=json_data)
    return response.status_code
