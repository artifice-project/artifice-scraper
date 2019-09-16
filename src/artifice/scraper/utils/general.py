
def headify(arg):
    '''
    Eliminates frustration resulting from the automatic formatting
    of request header keys.

    >>> headify('AUTH_TOKEN')
        'Auth-Token'

    # TODO::
    # >>> headify({'AUTH_TOKEN': 'Unchanged_Value'})
    #     {'Auth-Token': 'Unchanged_Value'}
    '''
    func = lambda x: '-'.join([_.title() for _ in x.split('_')])

    return func(arg)


def cmp_dict(before, after):
    reply = {}
    for key, val in after.items():
        if before.get(key) != val:
            reply.update({key: after.get(key)})
    return reply


def validate_auth(request):
    import logging
    from flask import request, current_app
    log = logging.getLogger(__name__)
    key = 'AUTH_TOKEN'
    if current_app.config.get('DEBUG'):
        return True
    client_token = request.headers.get(headify(key))
    if not client_token:
        return False
    server_token = current_app.config.get(key)
    if client_token != server_token:
        log.info(' * VALIDATION: MISMATCH (client:`{0}` != server:`{1}`)'.format(client_token, server_token))
        return False
    return True


def _side_load(data):
    reply = []
    for key, val in data.items():
        if isinstance(val, list):
            for each in val:
                reply.append({key:each})
        else:
            reply.append({key:val})
    return reply


def side_load(key, data):
    return _side_load({key: data.get(key)})


def setattrs(obj, **kwargs):
    for k, v in kwargs.items():
        setattr(obj, k, v)
    return obj


def force_json(obj):
    import json
    raw_json = json.dumps(obj, indent=4, sort_keys=True, default=str)
    safe_json = json.loads(raw_json)
    return safe_json


def git_sha():
    import git
    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha
    return sha
