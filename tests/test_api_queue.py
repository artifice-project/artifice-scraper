from tests import factories

endpoint = '/queue'


def test_get_returns_empty_queue(client, session):
    response = client.get(endpoint)

    assert response.status_code == 200
    assert 'msg' in response.json.keys()
    assert 'reply' in response.json.keys()


def test_post_data_raises_error_queue(client, session):
    bad_data = {'url': False, 'ahhhh': 'hHHhHHhHhH'}
    response = client.post(endpoint, json=bad_data)

    assert response.status_code == 422


def test_post_returns_single_item_queue(client, session):
    url = 'http://www.google.com'
    json_data = dict(url=url)
    response = client.post(endpoint, json=json_data)

    assert response.status_code == 200
    assert response.json[0].get('url') == url


def test_post_returns_many_items_queue(client, session):
    url1 = 'http://www.google.com'
    url2 = 'http://www.yahoo.com'
    json_data = dict(url=[url1, url2])
    response = client.post(endpoint, json=json_data)

    assert response.status_code == 200
    assert response.json[0].get('url') in (url1, url2)


def test_put_returns_success_queue(client, session):
    url = 'http://www.google.com'
    status = 'DONE'
    json_data = dict(url=url, status=status)
    response = client.put(endpoint, json=json_data)

    assert response.status_code == 200
    assert response.json.get('status') == status
    assert response.json.get('url') == url


def test_put_empty_raises_error_queue(client, session):
    response = client.put(endpoint)

    assert response.status_code == 400


def test_post_empty_raises_error_queue(client, session):
    response = client.post(endpoint)

    assert response.status_code == 400


def test_get_returns_specific_queue(client, session):
    response = client.get(endpoint + '/1')

    assert response.status_code == 404
