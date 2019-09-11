import pytest
import inspect
import subprocess
from flask_script import Command


class PytestCommand(Command):
    """
    Runs tests, to invoke natively run `pytest`
    """
    capture_all_args = True

    def __call__(self, app=None, *args):
        pytest.main(*args)

class CoverageCommand(Command):
    """
    Run a test coverage report.
    """
    capture_all_args = False

    def __call__(self, app=None):
        from .util import get_package_name
        pkg_name = get_package_name()
        cmd = 'py.test --cov-report term-missing --cov {0}'.format(pkg_name)
        subprocess.call(cmd, shell=True)
