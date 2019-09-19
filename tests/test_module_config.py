import pytest
import unittest.mock as mock


def test_constants_config():
    import artifice.scraper.config.constants as constants
    assert constants.__dict__


def test_local_config():
    import artifice.scraper.config.local as config
    # verify that required values are present
    assert config.__dict__


def test_staging_config():
    # config.staging uses environment variables, which should
    # NOT be assumed to be set during unittest. This is a crude
    # workaround to still allow import to be tested, since a
    # missing module will raise ImportError
    import os
    k = mock.patch.dict(os.environ,
        {
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///',
            'CELERY_BROKER_URL': 'sqlite:///',
            'AUTH_TOKEN': 'secretaccesstoken',
            'LOG_FILE': 'flask_temp.log'
        }
    )
    k.start()
    import artifice.scraper.config.staging as config
    # verify that required values are present
    assert config.__dict__
    k.stop()


def test_testing_config():
    import artifice.scraper.config.testing as config
    # verify that required values are present
    assert config.__dict__
