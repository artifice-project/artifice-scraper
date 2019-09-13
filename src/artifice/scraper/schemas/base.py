from flask import current_app
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields

import artifice.scraper.config.constants as constants

ma = Marshmallow()


class BaseSchema(ma.ModelSchema):
    id = fields.Int(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)


class BaseArgSchema(Schema):
    limit = fields.Int(required=False, default=10)
    limit = fields.Int(required=False, default=constants.ARGS_DEFAULT_LIMIT)
