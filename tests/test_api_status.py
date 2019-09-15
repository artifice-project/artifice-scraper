from tests import factories

endpoint = '/status'


def test_get_should_return_status(client, session):
    response = client.get(endpoint)

    assert response.status_code == 200
    assert 'enabled' in response.json.keys()
    assert 'polite' in response.json.keys()
    assert 'debug' in response.json.keys()


def test_post_missing_body_status(client, session):
    response = client.post(endpoint)

    assert response.status_code == 422
    assert 'error' in response.json


def test_post_should_change_status(client, session):
    enabled = True
    debug = True
    polite = 999
    json_data = dict(enabled=enabled, debug=debug, polite=polite)
    response = client.post(endpoint, json=json_data)

    assert response.status_code == 200
    assert response.json['enabled'] == enabled
    assert response.json['debug'] == debug
    assert response.json['polite'] == polite


def test_post_should_raise_error_status(client, session):
    enabled = 'hello world'
    debug = -4
    polite = False
    json_data = dict(enabled=enabled, debug=debug, polite=polite)
    response = client.post(endpoint, json=json_data)

    assert response.status_code == 422


def test_put_should_release_tasks_status(client, session):
    response = client.put(endpoint)

    assert response.status_code == 200
