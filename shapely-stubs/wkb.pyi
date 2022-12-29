from typing import Any, AnyStr, Protocol, overload

from typing_extensions import Literal

from ._typing import (
    _ArrayLikeAnyStr,
    _ArrayLikeGeometry,
    _NDArrayGeometry,
    _NDArrayObject,
)
from .geometry.base import BaseGeometry

class _Reader(Protocol):
    def read(self) -> str | bytes: ...

class _Writer(Protocol):
    def write(self, __s: str) -> Any: ...

@overload
def loads(data: AnyStr, hex: Literal[False] = ...) -> BaseGeometry: ...
@overload
def loads(data: _ArrayLikeAnyStr, hex: bool = ...) -> _NDArrayGeometry: ...
def load(fp: _Reader, hex: bool = ...): ...
@overload
def dumps(
    ob: BaseGeometry, hex: Literal[False] = ..., srid: int | None = ..., **kw
) -> bytes: ...
@overload
def dumps(
    ob: _ArrayLikeGeometry, hex: Literal[False] = ..., srid: int | None = ..., **kw
) -> _NDArrayObject: ...
@overload
def dumps(
    ob: BaseGeometry, hex: Literal[True], srid: int | None = ..., **kw
) -> str: ...
@overload
def dumps(
    ob: _ArrayLikeGeometry, hex: Literal[True], srid: int | None = ..., **kw
) -> _NDArrayObject: ...
def dump(ob: BaseGeometry, fp: _Writer, hex: bool = ..., **kw) -> None: ...
