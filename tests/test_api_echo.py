from tests import factories

endpoint = '/echo'


def test_get_echo_returns_defaults(client):
    response = client.get(endpoint)

    assert response.status_code == 200
    assert not response.json.get('args')
    assert not response.json.get('data')
    assert response.json.get('headers')


def test_get_echo_returns_data(client):
    key, val = 'foo', 'bar'
    json_data = {key: val}
    response = client.get(endpoint, json=json_data)

    assert response.status_code == 200
    assert response.json.get('data')[key] == val


def test_post_echo_returns_defaults(client):
    response = client.post(endpoint)

    assert response.status_code == 200
    assert not response.json.get('args')
    assert not response.json.get('data')
    assert response.json.get('headers')


def test_post_echo_returns_data(client):
    key, val = 'foo', 'bar'
    json_data = {key: val}
    response = client.post(endpoint, json=json_data)

    assert response.status_code == 200
    assert response.json.get('data')[key] == val
