from typing import Callable, Literal, overload

from numpy.typing import ArrayLike

from ._typing import _ArrayLikeFloat, _ArrayLikeGeometry, _NDArrayGeometry, _NDArrayInt
from .geometry.base import BaseGeometry

@overload
def transform(
    geometry: BaseGeometry,
    transformation: Callable[[ArrayLike], ArrayLike],
    include_z: bool = ...,
) -> BaseGeometry: ...
@overload
def transform(
    geometry: _ArrayLikeGeometry,
    transformation: Callable[[ArrayLike], ArrayLike],
    include_z: bool = ...,
) -> _NDArrayGeometry: ...
@overload
def transform(
    geometry: None,
    transformation: Callable[[ArrayLike], ArrayLike],
    include_z: bool = ...,
) -> None: ...
def count_coordinates(geometry: BaseGeometry | _ArrayLikeGeometry) -> int: ...
@overload
def get_coordinates(
    geometry: BaseGeometry | _ArrayLikeGeometry | None,
    include_z: bool = ...,
    return_index: Literal[False] = ...,
) -> _NDArrayGeometry: ...
@overload
def get_coordinates(
    geometry: BaseGeometry | _ArrayLikeGeometry | None,
    include_z: bool,
    return_index: Literal[True],
) -> tuple[_NDArrayGeometry, _NDArrayInt]: ...
@overload
def get_coordinates(
    geometry: BaseGeometry | _ArrayLikeGeometry | None,
    include_z: bool = ...,
    *,
    return_index: Literal[True],
) -> tuple[_NDArrayGeometry, _NDArrayInt]: ...
@overload
def set_coordinates(
    geometry: BaseGeometry, coordinates: _ArrayLikeFloat
) -> BaseGeometry: ...
@overload
def set_coordinates(
    geometry: _ArrayLikeGeometry, coordinates: _ArrayLikeFloat
) -> BaseGeometry: ...
