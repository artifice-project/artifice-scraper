from tests import factories

endpoint = '/health'


def test_get_health_returns_environment(client):
    response = client.get(endpoint)

    assert response.status_code == 200
    assert response.json.get('env') == 'testing'


def test_get_health_returns_commit_sha(client):
    response = client.get(endpoint)

    assert response.status_code == 200
    assert len(response.json.get('sha')) == 40
