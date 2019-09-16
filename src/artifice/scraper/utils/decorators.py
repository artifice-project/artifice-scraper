from flask import current_app
from flask import request
from functools import wraps

from .replies import (
    reply_empty,
    reply_unauthorized
)
from .general import validate_auth


# @requires_body
def requires_body(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if not request.data:
            return reply_empty(error='Request body cannot be empty')
        else:
            return f(*args, **kwargs)
    return wrap

# @auth
def auth(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if not validate_auth(request):
            return reply_unauthorized(error='Authentication required')
        else:
            return f(*args, **kwargs)
    return wrap
