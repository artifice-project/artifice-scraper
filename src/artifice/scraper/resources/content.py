import logging
from flask import current_app
from flask import request
from flask_restful import Resource

from artifice.scraper.models import db, Content
from artifice.scraper.utils import (
    auth,
    reply_success,
    reply_error,
    reply_empty,
    reply_conflict,
    requires_body,
)
from artifice.scraper.schemas import (
    content_schema,
    contents_schema,
    args_schema,
)

log = logging.getLogger(__name__)


class ContentResource(Resource):

    def get(self):
        '''
        displays the stored content from the database
        '''
        args, _ = args_schema.dump(request.get_json())
        result = db.session.query(Content).limit( \
                    args.get('limit')).all()
        data, _ = contents_schema.dump(result)
        return reply_success(msg=args, reply=data)

    @auth
    @requires_body
    def post(self):
        '''
        stores scraped content to the database
        '''
        data, errors = content_schema.load(request.get_json())
        if errors:
            log.error({__class__: errors})
            return reply_error(errors)
        elif data:
            result = db.session.query(Content).filter_by(origin=data.origin).first()
            if not result:
                db.session.add(data)
                db.session.commit()
                reply, _ = content_schema.dump(data)
                return reply_success(reply)
            reply, _ = content_schema.dump(result)
            return reply_conflict(reply)
        return reply_empty()
