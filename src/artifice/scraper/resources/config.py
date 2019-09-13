from flask import current_app
from flask import request, jsonify
from flask_restful import Resource


class ConfigResource(Resource):
    def get(self):
        cfg = current_app.config
        return jsonify(str(cfg))
