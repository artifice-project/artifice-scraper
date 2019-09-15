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
    reply_empty,
    side_load,
    send_to_celery,
)
from artifice.scraper.schemas import (
    queue_schema,
    queues_schema,
    queue_args_schema,
    queue_task_schema,
)
from artifice.scraper.supervisor import Supervisor

log = logging.getLogger(__name__)


class QueueResource(Resource):

    def get(self):
        '''
        show all url entries from the database
        '''
        args, _ = queue_args_schema.dump(request.get_json())
        result = db.session.query(Queue).filter(Queue.status.in_( \
                    args.get('status'))).limit( \
                    args.get('limit')).all()
        data, _ = queues_schema.dump(result)
        return reply_success(msg=args, reply=data)

    @auth
    @requires_body
    def post(self):
        '''
        post urls directly to the celery task queue
        '''
        json_data = side_load('url', request.get_json())
        data, errors = queues_schema.load(json_data)
        if errors:
            log.error({__class__: errors})
            return reply_error(errors)
        elif data:
            reply = []
            for each in data:
                result = db.session.query(Queue).filter_by(url=each.url).first()
                if not result:
                    log.info(' * RECEIVED {0}'.format(each.url))
                    db.session.add(each)
                    reply.append(queue_task_schema.dump(each).data)
                elif result:
                    log.debug(' * DUPLICATE: {0}'.format(each.url))
                    pass
            db.session.commit()
            for each in reply:
                if not Supervisor.status().get('debug'):
                    send_to_celery(each['url'])
                    log.info(' * TASKED {0}'.format(each['url']))
                else:
                    log.info(' * DEBUG MODE ENABLED {0}'.format(each['url']))
            return reply_success(reply)
        return reply_empty()

    @auth
    @requires_body
    def put(self):
        '''
        saves urls to queue database, used only by celery
        '''
        data, errors = queue_schema.load(request.get_json())
        if errors:
            log.error({__class__: errors})
            return reply_error(errors)
        elif data:
            log.debug(' * RETURNING {0}'.format(queue_schema.dump(data)))
            result = db.session.query(Queue).filter_by(url=data['url']).first()
            if result:
                result.status = data['status']
            else:
                log.error(' * UNEXPECTED {0}'.format(queue_schema.dump(data)))
                db.session.add(data)
            db.session.commit()
            reply, _ = queue_schema.dump(result)
            return reply_success(reply)
        return reply_empty()
