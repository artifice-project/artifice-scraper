from marshmallow import Schema, fields


class StatusSchema(Schema):
    enabled = fields.Boolean(required=False)
    debug = fields.Boolean(required=False)
    polite = fields.Number(required=False)


class SupervisorSchema(Schema):
    """
    Loads upon receiving the request JSON, performs validation
    and is used to GET/SET the redis_client values. Will raise
    an error only if attempting to write a valid field with an
    invalid type.
    """
    enabled =  fields.Int(required=False, strict=False)
    debug =    fields.Int(required=False, strict=False)
    polite =   fields.Int(required=False, strict=False)
