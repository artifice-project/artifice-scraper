from tests import factories

endpoint = '/metrics'


def test_get_metrics_returns_count(client, session):
    response = client.get(endpoint)

    assert response.status_code == 200
    assert response.json

    body = response.json

    assert body.get('queue')['total'] == 0
    assert body.get('queue')['READY'] == 0
    assert body.get('queue')['TASKED'] == 0
    assert body.get('queue')['DONE'] == 0
    assert body.get('content')['total'] == 0
