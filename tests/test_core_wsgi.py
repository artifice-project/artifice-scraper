import pytest


def test_core_wsgi_application():
    import artifice.scraper.core.wsgi as wsgi

    assert wsgi.application
