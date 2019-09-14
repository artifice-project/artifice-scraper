import logging
from flask import current_app
from flask import request, jsonify
from flask_restful import Resource

from artifice.scraper.supervisor import Supervisor
from artifice.scraper.utils import (
    auth,
    requires_body,
    reply_success,
    reply_error,
)
from artifice.scraper.models import db, Queue
from artifice.scraper.schemas import (
    status_schema,
    queues_schema,
)

log = logging.getLogger(__name__)


class StatusResource(Resource):

    def get(self):
        '''
        returns a json object containing status values
        '''
        msg = []
        status = Supervisor.status()
        return reply_success(msg=msg, **status)

    # @auth
    @requires_body
    def post(self):
        '''
        allows the status configuration values to be modified
        modified values are echoed back in the `msg` list
        '''
        data, errors = status_schema.load(request.get_json())
        if errors:
            log.error({__class__: errors})
            return reply_error(errors)
        elif data:
            changed = Supervisor.handle_changes(data)
            msg = Supervisor.render_msg(changed)
            status = Supervisor.status()
            log.debug(dict(changed=changed))
            return reply_success(msg=msg, **status)

    @auth
    def put(self):
        '''
        releases any waiting tasks to the queue for processing
        '''
        result = db.session.query(Queue).filter_by(status='READY').all()
        # for each in result, update status and release to celery
        # append to reply, return reply
        raise NotImplementedError()
