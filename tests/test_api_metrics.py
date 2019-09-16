from tests import factories

endpoint = '/metrics'


def test_get_metrics_returns_count(client, session):
    response = client.get(endpoint)

    assert response.status_code == 200
    assert response.json

    body = response.json

    assert type(body.get('queue')['total']) is int
    assert type(body.get('queue')['READY']) is int
    assert type(body.get('queue')['TASKED']) is int
    assert type(body.get('queue')['DONE']) is int
    assert type(body.get('content')['total']) is int
