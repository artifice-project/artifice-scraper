import logging
from flask import current_app
from flask import request
from flask_restful import Resource

from artifice.scraper.models import db, Content
from artifice.scraper.utils import (
    auth,
    reply_success,
    reply_error,
    reply_auto,
    requires_body,
)
from artifice.scraper.schemas import (
    content_schema,
    contents_schema,
    args_schema,
)

log = logging.getLogger(__name__)


class ContentResource(Resource):

    def get(self):
        '''
        displays the stored content from the database
        '''
        raise NotImplementedError()

    @auth
    @requires_body
    def post(self):
        '''
        stores scraped content to the database
        '''
        raise NotImplementedError()
