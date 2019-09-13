import logging
from flask import current_app
from flask import request
from flask_restful import Resource

from artifice.scraper.models import (
    db,
    Queue,
    Content,
)
from artifice.scraper.utils import (
    reply_success,
    # requests_per_minute,
)
from artifice.scraper.supervisor import Supervisor

log = logging.getLogger(__name__)


class MetricsResource(Resource):

    @staticmethod
    def queue_metrics():
        return dict(
            total=0,
            READY=0,
            TASKED=0,
            DONE=0,
        )

    @staticmethod
    def content_metrics():
        return dict(
            total=0,
        )

    def get(self):
        '''
        displays statistics on database size and request volume
        '''
        raise NotImplementedError()
