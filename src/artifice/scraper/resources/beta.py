from flask import current_app
from flask import request, jsonify
from flask_restful import Resource

from artifice.scraper.utils import (
    reply_success,
    send_to_celery,
)


class BetaResource(Resource):

    def get(self):
        r = send_to_celery()
        return reply_success(str(r))
