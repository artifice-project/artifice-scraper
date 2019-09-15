import pytest


def test_core_get_package_name():
    from artifice.scraper.core.util import get_package_name
    name = get_package_name()

    assert name in ('artifice', 'tests')
