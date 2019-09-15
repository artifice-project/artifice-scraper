from flask import current_app
from flask import request, jsonify
from flask_restful import Resource

from artifice.scraper.utils import force_json, auth


class ConfigResource(Resource):

    @auth
    def get(self):
        cfg = current_app.config
        msg = force_json(cfg)
        return jsonify(msg)
