import pytest


def test_module_import_etc():
    try:
        import artifice.etc
    except ImportError as e:
        raise e


def test_banners_version():
    from artifice.etc.banners import artifice_version
    version = artifice_version()

    assert version
    major, minor, micro = version.split('.')
    assert major.isnumeric()
    assert minor.isnumeric()
    assert micro.isnumeric()


def test_banners_logo():
    from artifice.etc.banners import artifice_logo
    logo = artifice_logo()

    assert isinstance(logo, str)


def test_banners_help():
    from artifice.etc.banners import artifice_help
    help = artifice_help()

    assert isinstance(help, str)


def test_terminal_output():
    import io
    from contextlib import redirect_stdout
    f = io.StringIO()
    test_string = 'hello world'
    with redirect_stdout(f):
        from artifice.etc.render import terminal_output
        terminal_output(test_string)

    assert test_string in f.getvalue()


def test_welcome_message():
    import io
    from contextlib import redirect_stdout
    f = io.StringIO()
    with redirect_stdout(f):
        from artifice.etc import welcome
        welcome()

    assert len(f.getvalue()) > 0
