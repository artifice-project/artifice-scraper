def cmp_dict(before, after):
    reply = {}
    for key, val in after.items():
        if before.get(key) != val:
            reply.update({key: after.get(key)})
    return reply

def validate_auth(request):
    from flask import request, current_app
    client_token = request.headers.get('AUTH_TOKEN')
    if not client_token:
        return False
    server_token = current_app.config.get('AUTH_TOKEN')
    if client_token != server_token:
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

# def json_serial(obj):
#     from datetime import date, datetime
#     '''
#     JSON serializer for objects not serializable by default `jsonify` function
#     '''
#     if isinstance(obj, (datetime, date)):
#         return obj.isoformat()
#     raise TypeError('Type {0} not serializable'.format(type(obj)))
