def test_send_to_celery_returns_async_result():
    from artifice.scraper.utils import send_to_celery
    from celery.result import AsyncResult
    url = 'http://www.google.com/'
    uid = send_to_celery(url)
    assert uid
    assert isinstance(uid, AsyncResult)
