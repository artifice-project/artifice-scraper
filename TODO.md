# To Do
- Convert Supervisor to either Redis or single-object state
- Add scheduled database dumps and backups
- Add alerts and critical messaging, for process status, disk use, etc
```text
On scheduled intervals, the same checks which are performed within the /health endpoint
should be performed automatically. In such a case that a service is either unavailable or
stopped, a notification shall be sent to a designated party. Once the notification has been sent,
the system will continue to poll for health but will NOT send a duplicate message regarding
the same service status message. In such a case that an additional service changes status after
having sent an alert, that alert shall be sent. Once restarted, the system will again send an alert
if the service again goes down.
```
- Ability to view a specific entry by its ID
- ability to disown/remove orphan tasks
-
