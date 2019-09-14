HOST = '127.0.0.1'
AUTH_TOKEN = 'correcthorsebatterystaple'

SUPERVISOR_DEBUG = False
SUPERVISOR_ENABLED = True
SUPERVISOR_POLITE = 10

ARGS_DEFAULT_LIMIT = 10
ARGS_DEFAULT_STATUS = ['READY', 'TASKED', 'DONE']

URL_FOR_STATUS = 'http://{}/status'.format(HOST)
URL_FOR_QUEUE = 'http://{}/queue'.format(HOST)
URL_FOR_CONTENT = 'http://{}/content'.format(HOST)
