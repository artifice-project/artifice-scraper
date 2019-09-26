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
)
from artifice.scraper.supervisor import Supervisor

log = logging.getLogger(__name__)


class MetricsResource(Resource):

    @staticmethod
    def queue_metrics():
        return dict(
            total=db.session.query(Queue).count(),
            READY=db.session.query(Queue).filter_by(status='READY').count(),
            TASKED=db.session.query(Queue).filter_by(status='TASKED').count(),
            DONE=db.session.query(Queue).filter_by(status='DONE').count(),
        )

    @staticmethod
    def content_metrics():
        return dict(
            total=db.session.query(Content).count(),
        )

    @staticmethod
    def idle_ratio(q):
        done = q['DONE']
        ready = q['READY']
        tasked = q['TASKED']
        try:
            ratio = (tasked + ready) / done
        except ZeroDivisionError:
            ratio = 0
        return round(ratio, 2)

    def get(self):
        '''
        displays statistics on database size, can also be used for
        Redis values and uptime.
        '''
        q = self.queue_metrics()
        c = self.content_metrics()
        database = dict(queue=q, content=c)
        i = self.idle_ratio(q)
        ratio = dict(idle=i)
        return reply_success(database=database, ratio=ratio)
