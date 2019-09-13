from flask import current_app
from flask import request, jsonify
from flask_restful import Resource

from artifice.scraper.supervisor import Supervisor
from artifice.scraper.utils import requires_body, auth


class StatusResource(Resource):

    def get(self):
        status = Supervisor.status()
        return jsonify(status)

    # @auth
    @requires_body
    def post(self):
        data = request.get_json()
        changed = Supervisor.handle_changes(data)
        msg = Supervisor.render_msg(changed)
        return jsonify(msg)
