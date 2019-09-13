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

                        𝕐𝕠𝕦 𝔸𝕣𝕖 𝕎𝕙𝕒𝕥 𝕐𝕠𝕦 𝕊𝕖𝕖
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
