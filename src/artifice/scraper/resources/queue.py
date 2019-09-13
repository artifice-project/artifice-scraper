import logging
from flask import current_app
from flask import request
from flask_restful import Resource

from artifice.scraper.models import db, Queue
from artifice.scraper.utils import (
    auth,
    requires_body,
    reply_success,
    reply_error,
    reply_auto,
    side_load,
)
from artifice.scraper.schemas import (
    queue_args_schema,
    queue_schema,
    queues_schema,
    queue_task_schema,
)
from artifice.scraper.supervisor import Supervisor

log = logging.getLogger(__name__)


class QueueResource(Resource):

    def get(self):
        '''
        show all url entries from the database
        '''
        raise NotImplementedError()

    @auth
    @requires_body
    def post(self):
        '''
        post urls directly to the celery task queue
        '''
        raise NotImplementedError()

    @auth
    @requires_body
    def put(self):
        '''
        saves urls to queue database, used only by celery
        '''
        raise NotImplementedError()
