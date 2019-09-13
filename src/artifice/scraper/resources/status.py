import logging
from flask import current_app
from flask import request, jsonify
from flask_restful import Resource

from artifice.scraper.supervisor import Supervisor
from artifice.scraper.utils import (
    requires_body,
    auth,
    reply_success,
    reply_error,
)
from artifice.scraper.schemas import status_schema

log = logging.getLogger(__name__)


class StatusResource(Resource):

    def get(self):
        msg = []
        status = Supervisor.status()
        return reply_success(msg=msg, **status)

    # @auth
    @requires_body
    def post(self):
        data, errors = status_schema.load(request.get_json())
        if errors:
            log.error({__class__: errors})
            return reply_error(errors)
        elif data:
            changed = Supervisor.handle_changes(data)
            log.debug(dict(changed=changed))
            msg = Supervisor.render_msg(changed)
            status = Supervisor.status()
            return reply_success(msg=msg, **status)

    @auth
    def put(self):
        raise NotImplementedError()
