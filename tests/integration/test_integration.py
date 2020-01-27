# https://stackoverflow.com/questions/40880259/how-to-pass-arguments-in-pytest-by-command-line
import os
import pytest
import requests

TIMEOUT = 10
HEADERS = {"Auth-Token": "supersecrettoken"}

@pytest.fixture()
def testhost(pytestconfig):
    # This setup is called before EVERY test in this module
    ipAddress = pytestconfig.getoption("testhost")
    if ipAddress is None:
        pytest.exit("Must provide IP address with --testhost")
    if not ipAddress.startswith("http"):
        ipAddress = "http://{}".format(ipAddress)
    return ipAddress


@pytest.mark.integration
def test_integration_canary(testhost):
    # This function does not perform any test, it only exists
    # as the first function to be called within this module so
    # checks performed within the 'testhost' fixture are called.
    pass


@pytest.mark.integration
def test_integration_status(testhost):
    url = os.path.join(testhost, "status")
    body = dict(debug=0, enabled=1, polite=5)
    r = requests.post(url, json=body, headers=HEADERS)
    assert r.status_code == 200
    assert r.json()["polite"] == body["polite"]


@pytest.mark.integration
def test_integration_seed(testhost):
    pass
