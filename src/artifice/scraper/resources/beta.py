from flask import current_app
from flask import request, jsonify
from flask_restful import Resource

from artifice.scraper.utils import reply_success


class BetaResource(Resource):

    def get(self):
        from artifice.scraper.tasks import callable_task
        r = callable_task.delay()
        return reply_success(str(r))
