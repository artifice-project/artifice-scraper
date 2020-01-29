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
    reply_empty,
    send_to_celery,
)
from artifice.scraper.models import db, Queue
from artifice.scraper.schemas import (
    status_schema,
    queues_schema,
    args_schema,
    supervisor_schema,
)

log = logging.getLogger(__name__)


class StatusResource(Resource):

    def get(self):
        '''
        returns a json object containing status values
        '''
        msg = []
        status, _ = supervisor_schema.dump(Supervisor.status())
        return reply_success(msg=msg, **status)

    @auth
    @requires_body
    def post(self):
        '''
        allows the status configuration values to be modified
        modified values are echoed back in the `msg` list
        # TODO: unify how we are calling the SupervisorSchemas
        '''
        data, errors = supervisor_schema.load(request.get_json())
        if errors:
            log.error({__class__: errors})
            return reply_error(errors)
        elif data:
            changed = Supervisor.update(data)
            msg = Supervisor.render_msg(changed)
            status = Supervisor.status()
            return reply_success(msg=msg, **status)
        return reply_empty()

    @auth
    def put(self):
        '''
        releases any waiting tasks to the queue for processing
        # TODO: figure out what is gonna be the best way to do this in a controlled manner
        '''
        args, _ = args_schema.dump(request.get_json())
        result = db.session.query(Queue).filter_by(status='READY').limit(args['limit']).all()
        for each in result:
            each.status = 'TASKED'
            if not Supervisor.status(key='debug'):
                send_to_celery(each.url)
                log.debug('[RELEASED] {}'.format(each.url))
            else:
                log.debug('[DEBUG] {}'.format(each.url))
        db.session.commit()
        reply = queues_schema.dump(result).data
        return reply_success(msg=args, reply=reply)
