def artifice_logo(*args, **kwargs):
    """
    http://patorjk.com/software/taag/#p=display&f=Block&t=artifice
    `Block` font
    """
    return \
"""

                       _|      _|      _|_|  _|
   _|_|_|  _|  _|_|  _|_|_|_|        _|            _|_|_|    _|_|
 _|    _|  _|_|        _|      _|  _|_|_|_|  _|  _|        _|_|_|_|
 _|    _|  _|          _|      _|    _|      _|  _|        _|
   _|_|_|  _|            _|_|  _|    _|      _|    _|_|_|    _|_|_|


"""

def artifice_help(*args, **kwargs):
    """
    // This text appears exactly as written below
    """
    return \
"""
[Usage]
artifice.scraper --help
artifice.maker --help
artifice.paper --help

[Website]
https://artifice-project.com

[Source]
https://github.com/artifice-project/artifice-scraper

 * this message is displayed automatically, no arguments are parsed
"""

def artifice_version(*args, **kwargs):
    import pkg_resources
    ver = pkg_resources.get_distribution("Artifice").version
    return "Version " + ver


def main(*args):
    import sys
    ver = artifice_version()
    logo = artifice_logo()
    help = artifice_help()
    print(ver, logo, help, file=sys.stderr)
    sys.exit(0)


if __name__ == '__main__':
    main()
