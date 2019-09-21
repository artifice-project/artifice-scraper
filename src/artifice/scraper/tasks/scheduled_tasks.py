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
    from artifice.scraper.redis import alert_if_service_stopped
    services = ['celeryd', 'postgresql', 'rabbitmq-server', 'redis-server']
    reply = []
    for service in services:
        tb = alert_if_service_stopped(service)
        print({service: tb})
        reply.append(tb)
    # from .callable_tasks import sms_notify
    # sms_notify(tb)
