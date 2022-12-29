from typing import Any, AnyStr, Protocol, overload

from shapely.geometry.base import BaseGeometry

from ._typing import _ArrayLikeAnyStr, _ArrayLikeGeometry, _NDArrayGeometry

class _Reader(Protocol):
    def read(self) -> str | bytes: ...

class _Writer(Protocol):
    def write(self, __s: str) -> Any: ...

@overload
def loads(data: AnyStr) -> BaseGeometry: ...
@overload
def loads(data: _ArrayLikeAnyStr) -> _NDArrayGeometry: ...
def load(fp: _Reader) -> BaseGeometry: ...
@overload
def dumps(
    ob: BaseGeometry, trim: bool = ..., rounding_precision: int = ..., **kw
) -> str: ...
@overload
def dumps(
    ob: _ArrayLikeGeometry, trim: bool = ..., rounding_precision: int = ..., **kw
) -> _NDArrayGeometry: ...
def dump(ob: BaseGeometry, fp: _Writer, **settings) -> None: ...
