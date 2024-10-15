from .functions1 import *  # noqa

try:
    from importlib.metadata import version, PackageNotFoundError  # Python 3.8+
    from  functools import cache
except ImportError:  # For Python < 3.8
    from importlib_metadata import version, PackageNotFoundError

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    # package is not installed
    pass
