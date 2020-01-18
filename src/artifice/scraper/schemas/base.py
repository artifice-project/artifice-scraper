from flask import current_app
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields, post_dump

import artifice.scraper.config.constants as constants

ma = Marshmallow()


class BaseSchema(ma.ModelSchema):
    id = fields.Int(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)


class BaseArgSchema(Schema):
    limit = fields.Int(required=False, default=constants.ARGS_DEFAULT_LIMIT)


class PaginationSchema(Schema):
    """
    Used to control the index and amount of `content` resources shown
    by means of request arguments. This allows pagination without the
    need for a JSON request body, allowing control from a web browser.

    Schema enforces the following rules, in order:
        - If no ``begins`` arg is provided, value defaults to 1
        - If no ``ends`` arg is provided, value defaults to 10
        - If ``begins`` is greater than ``ends``, values are switched
    """
    begins = fields.Int(required=False, strict=False, default=1)
    ends = fields.Int(required=False, strict=False, default=10)

    @post_dump
    def _post_dump(self, data, **kwargs):
        """ Correct improperly-ordered params """
        if data["begins"] > data["ends"]:
            tmp = data["ends"]
            data["ends"] = data["begins"]
            data["begins"] = tmp
        return data
