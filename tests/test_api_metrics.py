from tests import factories

endpoint = '/metrics'


def test_get_metrics_returns_count(client, session):
    response = client.get(endpoint)

    assert response.status_code == 200
    assert response.json

    body = response.json
    database = body['database']

    assert type(database.get('queue')['total']) is int
    assert type(database.get('queue')['READY']) is int
    assert type(database.get('queue')['TASKED']) is int
    assert type(database.get('queue')['DONE']) is int
    assert type(database.get('content')['total']) is int
