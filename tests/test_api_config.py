from tests import factories

endpoint = '/config'


def test_get_config_returns_object(client):
    response = client.get(endpoint)

    assert response.status_code == 200
    assert response.json
