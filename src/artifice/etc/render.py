def terminal_output(*args):
    import sys
    print(*args, file=sys.stdout)
    # sys.exit(0)

def welcome():
    from artifice.etc.banners import (
        artifice_version,
        artifice_logo,
        artifice_help,
    )
    return terminal_output(
        artifice_version(),
        artifice_logo(),
        artifice_help(),
    )
