'''
This module is used in conjunction with ../tasks/scheduled_tasks.py to monitor the state of daemon processes critical to the operation of the application. If a service is detected to have stopped, a check is performed to see whether or not this is the first detection of such an event. If it is--by merit of no key for that service--a notification (sms) is sent to the webmaster. Once the service is back online, the key is removed and the cycle repeats.

Scenario 1:
    Service:    RUNNING
    Key-Val:    MISSING
    Action: No further action required.

Scenario 2:
    Service:    RUNNING
    Key-Val:    PRESENT
    Action: The stored key-value pair corresponding to that service should be deleted, or set to False. No further action required.

Scenario 3:
    Service:    STOPPED
    Key-Val:    PRESENT
    Action: The webmaster has already been notified of this stoppage. No further action required.

Scenario 4:
    Service:    STOPPED
    Key-Val:    MISSING
    Action: This is the first detection of the stoppage. The key-value corresponding to the service should be set to True, and an SMS message sent to notify the webmaster of this change in state.
'''
from .base import redis_client
from artifice.scraper.utils import is_service_running

# service_list = ['celeryd', 'postgresql', 'rabbitmq-server', 'redis-server']


def alert_if_service_stopped(service):
    from flask import current_app
    if current_app.env != 'production':
        return
    reply = []
    key = 'SERVICE_ALERTED_{0}'.format(service)
    reply.append({'key': key})

    if is_service_running(service) != 'running':
        alert_sent = redis_client.get(key)
        reply.append({'alert_sent': alert_sent})
        if alert_sent:
            pass
        else:
            reply.append(' * THIS IS WHERE WE WOULD SENT A MESSAGE')
            # async_task.delay(service)
            redis_client.set(key, 1)
    else:
        redis_client.set(key, None)
        reply.append(' * no further action')
    # except redis.exceptions.ConnectionError as e:
