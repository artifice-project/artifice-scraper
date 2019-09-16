import pytest


def test_utils_system_number_of_cores():
    from artifice.scraper.utils import number_of_cores
    num = number_of_cores()

    assert isinstance(num, int)


def test_utils_system_time_of_deployment():
    from artifice.scraper.utils import time_of_deployment
    tm = time_of_deployment()

    assert tm


def test_utils_system_is_service_running():
    from artifice.scraper.utils import is_service_running
    ps = 'sshd'
    tf = is_service_running(ps)

    assert tf in ('running', 'stopped', 'unavailable')
