from typing import TypeVar

from . import lib as lib
from .errors import UnsupportedGEOSVersionError as UnsupportedGEOSVersionError

_T = TypeVar("_T")

class requires_geos:
    version: str
    def __init__(self, version: str) -> None: ...
    def __call__(self, func: _T) -> _T: ...

def multithreading_enabled(func: _T) -> _T: ...
