HOST = '127.0.0.1'
PORT = 5000
AUTH_TOKEN = 'correcthorsebatterystaple'

SUPERVISOR_DEBUG = False
SUPERVISOR_ENABLED = True
SUPERVISOR_POLITE = 1

ARGS_DEFAULT_LIMIT = 10
ARGS_DEFAULT_STATUS = ['READY', 'TASKED', 'DONE']

URL_FOR_STATUS = 'http://{0}:{1}/status'.format(HOST, PORT)
URL_FOR_QUEUE = 'http://{0}:{1}/queue'.format(HOST, PORT)
URL_FOR_CONTENT = 'http://{0}:{1}/content'.format(HOST, PORT)
