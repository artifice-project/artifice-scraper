import pytest
import os
import unittest.mock as mock


def test_create_app_from_envvar():
    k = mock.patch.dict(os.environ,
        {
            'FLASK_CONFIG_PATH': '../config/local.py',
        }
    )
    k.start()
    from artifice.scraper.core.app import create_app
    app = create_app()
    k.stop()


def test_create_app_settings_override():
    from artifice.scraper.core.app import create_app
    key1, val1 = 'FOO', 'foo'
    key2, val2 = 'BAR', 'bar'
    settings_override = {
        key1: val1,
        key2: val2,
    }
    app = create_app(settings_override=settings_override)
    assert app.config[key1] == val1
    assert app.config[key2] == val2


def test_create_app_with_log_file():
    from artifice.scraper.core.app import create_app
    key, val = 'LOG_FILE', 'flask_test.log'
    settings_override = {
        key: val,
    }
    app = create_app(settings_override=settings_override)
    assert app.config[key] == val
    assert os.path.exists(val)
    # bodge: remove the created file
    os.remove(val)


def test_create_celery_app():
    from artifice.scraper.core.app import create_celery_app
    celery_app = create_celery_app()

    assert celery_app
