import logging
from flask import current_app
from flask import request, jsonify
from flask_restful import Resource

from artifice.scraper.utils import reply_success

log = logging.getLogger(__name__)

def echo_request(request):
    data = request.get_json()
    args = request.args
    headers = dict(request.headers)
    response = dict(data=data, args=args, headers=headers)
    return response


class EchoResource(Resource):

    def get(self):
        '''
        Returns values as they are received
        '''
        response = echo_request(request)
        log.debug(response)
        return reply_success(**response)

    def post(self):
        '''
        Returns values as they are received
        '''
        response = echo_request(request)
        log.debug(response)
        return reply_success(**response)
