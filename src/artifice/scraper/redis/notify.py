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
