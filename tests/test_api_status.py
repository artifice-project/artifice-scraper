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

    assert response.status_code == 400
    assert 'error' in response.json


def test_post_should_change_enabled_status(client, session):
    json_data = {'enabled': True}
    response = client.post(endpoint, json=json_data)

    assert response.status_code == 200
    assert response.json['enabled'] == True

    json_data = {'enabled': False}
    response = client.post(endpoint, json=json_data)

    assert response.status_code == 200
    assert response.json['enabled'] == False




def test_post_should_change_debug_status(client, session):
    json_data = {'debug': True}
    response = client.post(endpoint, json=json_data)

    assert response.status_code == 200
    assert response.json['debug'] == True

    json_data = {'debug': False}
    response = client.post(endpoint, json=json_data)

    assert response.status_code == 200
    assert response.json['debug'] == False


def test_post_should_change_polite_status(client, session):

    json_data = {'polite': 42}
    response = client.post(endpoint, json=json_data)

    assert response.status_code == 200
    assert response.json['polite'] == 42

    json_data = {'polite': 2}
    response = client.post(endpoint, json=json_data)

    assert response.status_code == 200
    assert response.json['polite'] == 2


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
