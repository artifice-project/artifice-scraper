from termcolor import colored

def artifice_logo(*args, **kwargs):
    """
    http://patorjk.com/software/taag/#p=display&f=Block&t=artifice
    `Block` font
    """
    color = "blue"
    text = \
"""

                       _|      _|      _|_|  _|
   _|_|_|  _|  _|_|  _|_|_|_|        _|            _|_|_|    _|_|
 _|    _|  _|_|        _|      _|  _|_|_|_|  _|  _|        _|_|_|_|
 _|    _|  _|          _|      _|    _|      _|  _|        _|
   _|_|_|  _|            _|_|  _|    _|      _|    _|_|_|    _|_|_|

                        𝕐𝕠𝕦 𝔸𝕣𝕖 𝕎𝕙𝕒𝕥 𝕐𝕠𝕦 𝕊𝕖𝕖
"""
    return colored(text, color)

def artifice_help(*args, **kwargs):
    """
    // This text appears exactly as written below
    """
    color = "white"
    text = \
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
    return colored(text, color)

def artifice_version(*args, **kwargs):
    import pkg_resources
    text = pkg_resources.get_distribution("Artifice").version
    color = "magenta"
    return colored(text, color)
