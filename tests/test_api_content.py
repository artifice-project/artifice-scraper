from tests import factories

endpoint = '/content'


def test_get_returns_empty_content(client, session):
    response = client.get(endpoint)

    assert response.status_code == 200
    assert 'msg' in response.json.keys()
    assert 'reply' in response.json.keys()


def test_post_returns_single_item_content(client, session):
    json_data = {
        'origin': 'http://www.google.com',
        'title': 'headline',
        'captions': ['photo', 'caption'],
        'text': 'hello world',
    }
    response = client.post(endpoint, json=json_data)

    assert response.status_code == 200
    assert response.json.get('origin') == json_data['origin']
    assert response.json.get('title') == json_data['title']
    assert response.json.get('captions') == json_data['captions']
    assert response.json.get('text') == json_data['text']


def test_post_returns_error_content(client, session):
    json_data = {
        'captions': ['photo', 'caption'],
        'text': True,
    }
    response = client.post(endpoint, json=json_data)

    assert response.status_code == 422


def test_get_returns_specific_content(client, session):
    response = client.get(endpoint + '/1')

    assert response.status_code == 200


def test_get_returns_pagination_content(client, session):
    # provide valid args
    urlencoding = '?begins=9&ends=11'
    response = client.get(endpoint+urlencoding)
    assert response.status_code == 200
    assert response.json.get('msg')['begins'] == 9
    assert response.json.get('msg')['ends'] == 11

    # provide reversed arguments
    urlencoding = '?begins=11&ends=9'
    response = client.get(endpoint+urlencoding)
    assert response.status_code == 200
    assert response.json.get('msg')['begins'] == 9
    assert response.json.get('msg')['ends'] == 11
