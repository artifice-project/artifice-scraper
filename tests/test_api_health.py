from tests import factories

endpoint = '/health'


def test_get_health_returns_environment(client):
    response = client.get(endpoint)

    assert response.status_code == 200
    assert response.json.get('environment') == 'testing'


def test_get_health_returns_commit_sha(client):
    response = client.get(endpoint)

    assert response.status_code == 200
    assert len(response.json.get('commit')) == 40


def test_get_health_returns_deployment_time(client):
    response = client.get(endpoint)

    assert response.status_code == 200
    assert response.json.get('deployed')


def test_get_health_returns_version(client):
    response = client.get(endpoint)

    assert response.status_code == 200
    assert response.json.get('version')
