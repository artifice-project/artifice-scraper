from artifice.scraper.tasks.base import celery_app


@celery_app.task(name='tasks.scheduled_task')
def scheduled_task():
    from flask import current_app
    env = current_app.config.get('ENV', '<missing>')
    print(' * Heartbeat (config:{0})'.format(env))


@celery_app.task(name='tasks.health_check')
def health_check():
    '''
    Function runs at specified interval and checks the status
    of a defined list of systemd services. Useful for early
    detection of errors and problems without the need to
    constantly monitor the API manually. This functionality
    is only really necessary in production environments,
    since during development the services are run without
    the use of daemons. In order to prevent repeated notification
    of the same status, once a message is sent informing of a status
    change, that service is stored in Redis as having been notified.
    Once the service is restarted, the key-value store is reset.
    '''
    # 1. check the status of the service, either by calling the is_running function
    #   directly or by fetching the /health endpoint and parsing the result.
    # 2. if service is not running, either 'unavailable' or 'stopped', then check
    #   the cache to see if a notification regarding that service has already been sent.
    # 3. if no notification has been sent, release the service and status to the send_message
    #   task in a non-blocking manner.
    # 4. if a notification has already been sent, no futher action should be taken.
    # 5. 
    pass
