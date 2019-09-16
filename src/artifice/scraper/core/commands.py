import pytest
import inspect
import subprocess
from flask_script import Command


def get_package_name():
    import inspect
    try:
        pkg = inspect.getmodule(inspect.stack()[1][0]).__name__
        return pkg.split('.')[0]
    except AttributeError as err:
        raise AttributeError('{0}\nFunction must be called from within another module to return a valid result'.format(str(err)))


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
        pkg_name = get_package_name()
        cmd = 'py.test --cov-report term-missing --cov {0}'.format(pkg_name)
        subprocess.call(cmd, shell=True)
