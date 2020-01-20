# '''
# This module is used in conjunction with ../tasks/scheduled_tasks.py to monitor the state of daemon processes critical to the operation of the application. If a service is detected to have stopped, a check is performed to see whether or not this is the first detection of such an event. If it is--by merit of no key for that service--a notification (sms) is sent to the webmaster. Once the service is back online, the key is removed and the cycle repeats.
#
# Scenario 1:
#     Service:    RUNNING
#     Key-Val:    MISSING
#     Action: No further action required.
#
# Scenario 2:
#     Service:    RUNNING
#     Key-Val:    PRESENT
#     Action: The stored key-value pair corresponding to that service should be deleted, or set to False. No further action required.
#
# Scenario 3:
#     Service:    STOPPED
#     Key-Val:    PRESENT
#     Action: The webmaster has already been notified of this stoppage. No further action required.
#
# Scenario 4:
#     Service:    STOPPED
#     Key-Val:    MISSING
#     Action: This is the first detection of the stoppage. The key-value corresponding to the service should be set to True, and an SMS message sent to notify the webmaster of this change in state.
# '''
# from .base import redis_client
#
#
# def internal_get_request(endpoint):
#     import requests
#     import os.path as osp
#     from flask import current_app
#     host = current_app.config['HOST']
#     url = osp.join(host, endpoint)
#     r = requests.get(url)
#     if r.status_code != 200:
#         raise ConnectionError('Unable to reach {0} \nStatus: {1} \nData: {2}'.format(url, r.status_code, r.json))
#     return r.json()
#
#
# def check_if_should_alert(service, status):
#     '''
#     1. Check if Redis store contains a record of this service being known to be down
#         > If known, return with no further action
#         > Else, store a record in Redis
#     2. Return the name of the service that is down <string>
#     The names of interrupted services will be appended to a list, from which an alert message will be constructed.
#     '''
#     key = 'SERVICE_ALERTED_{0}'.format(service)
#     if status == 'running':
#         redis_client.delete(key)
#         return
#     alerted = redis_client.get(key)
#     if alerted:
#         return
#     redis_client.set(key, 1)
#     return service
#
#
# def create_msg_body(reply):
#     '''
#     `reply` is a list of services which are not currently running.
#     Function creates a generic text blob which is passed to the
#     task which actually sends the alert message out.
#     '''
#     body = '[AWS] The following services are experiencing interruption: {0}'.format(reply)
#     return body
