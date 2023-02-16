from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("gdr4mock")
except PackageNotFoundError:
    # package is not installed
    pass