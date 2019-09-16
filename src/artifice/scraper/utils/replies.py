from flask import make_response, jsonify

def reply_success(*args, **kwargs):
    return make_response(jsonify(*args, **kwargs), 200)


def reply_error(*args, **kwargs):
    return make_response(jsonify(*args, **kwargs), 422)


def reply_conflict(*args, **kwargs):
    return make_response(jsonify(*args, **kwargs), 409)


def reply_unauthorized(*args, **kwargs):
    return make_response(jsonify(*args, **kwargs), 401)


def reply_empty(*args, **kwargs):
    return make_response(jsonify(*args, **kwargs), 400)
