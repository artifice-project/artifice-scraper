import logging
from flask import current_app
from flask import request, abort
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

    def get(self, _id=None):
        '''
        displays the stored content from the database
        uses request body to provide query args
        '''
        if _id:
            return self.get_one(_id)
        args, _ = args_schema.dump(request.get_json())
        result = db.session.query(Content).limit( \
                    args.get('limit')).all()
        data, _ = contents_schema.dump(result)
        return reply_success(msg=args, reply=data)

    def get_one(self, _id):
        '''
        displays a specific content result by database ID.
        if no such entry exists, a 404 error is raised.
        '''
        result = db.session.query(Content).filter_by(id=_id).first()
        if not result:
            abort(404)
        data, _ = content_schema.dump(result)
        return reply_success(data)

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
