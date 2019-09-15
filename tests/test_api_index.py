from tests import factories

endpoint = '/'


def test_get_should_return_index(client, session):
    response = client.get(endpoint)

    assert response.status_code == 200
    elem = response.json.pop()
    assert elem
    assert 'rule' in elem.keys()
    assert 'methods' in elem.keys()
    assert 'endpoint' in elem.keys()
