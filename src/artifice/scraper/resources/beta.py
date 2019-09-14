from flask import current_app
from flask import request, jsonify
from flask_restful import Resource


class BetaResource(Resource):

    def get(self):
        raise NotImplementedError()
