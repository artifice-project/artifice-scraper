import logging
from flask import current_app
from flask import request, jsonify
from flask_restful import Resource

from artifice.scraper.utils import reply_success

log = logging.getLogger(__name__)


class EchoResource(Resource):

    def get(self):
        '''
        Returns values as they are received
        '''
        data = request.get_json()
        args = request.args
        headers = dict(request.headers)
        response = dict(data=data, args=args, headers=headers)
        log.debug(response)
        return reply_success(**response)

    def post(self):
        '''
        Returns values as they are received
        '''
        data = request.get_json()
        args = request.args
        headers = dict(request.headers)
        response = dict(data=data, args=args, headers=headers)
        log.debug(response)
        return reply_success(**response)
