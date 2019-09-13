from marshmallow import fields

import artifice.scraper.config.constants as constants
from .base import BaseArgSchema
from .custom import Uppercase


class QueueArgsSchema(BaseArgSchema):
    status = fields.List(Uppercase(required=False), default=constants.ARGS_DEFAULT_STATUS)


# class ContentArgsSchema(BaseArgSchema):
