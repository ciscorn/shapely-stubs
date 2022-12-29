from typing import overload

import numpy
from shapely.geometry import Point
from shapely.geometry.base import BaseGeometry

from ._typing import (
    _ArrayLikeFloat,
    _ArrayLikeGeometry,
    _NDArrayFloat,
    _NDArrayGeometry,
)

@overload
def line_interpolate_point(
    line: BaseGeometry, distance: float, normalized: bool = ..., **kwargs
) -> Point: ...
@overload
def line_interpolate_point(
    line: _ArrayLikeGeometry,
    distance: float | _ArrayLikeFloat,
    normalized: bool = ...,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def line_interpolate_point(
    line: BaseGeometry | _ArrayLikeGeometry,
    distance: _ArrayLikeFloat,
    normalized: bool = ...,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def line_locate_point(
    line: BaseGeometry, other: Point, normalized: bool = ..., **kwargs
) -> numpy.float64: ...
@overload
def line_locate_point(
    line: _ArrayLikeGeometry,
    other: Point | _ArrayLikeGeometry,
    normalized: bool = ...,
    **kwargs
) -> _NDArrayFloat: ...
@overload
def line_locate_point(
    line: BaseGeometry | _ArrayLikeGeometry,
    other: _ArrayLikeGeometry,
    normalized: bool = ...,
    **kwargs
) -> _NDArrayFloat: ...
@overload
def line_merge(line: BaseGeometry, directed: bool = ..., **kwargs) -> BaseGeometry: ...
@overload
def line_merge(
    line: _ArrayLikeGeometry, directed: bool = ..., **kwargs
) -> _NDArrayGeometry: ...
@overload
def shared_paths(a: BaseGeometry, b: BaseGeometry, **kwargs) -> BaseGeometry: ...
@overload
def shared_paths(
    a: _ArrayLikeGeometry, b: BaseGeometry | _ArrayLikeGeometry, **kwargs
) -> _NDArrayGeometry: ...
@overload
def shared_paths(
    a: BaseGeometry | _ArrayLikeGeometry, b: _ArrayLikeGeometry, **kwargs
) -> _NDArrayGeometry: ...
@overload
def shortest_line(a: BaseGeometry, b: BaseGeometry, **kwargs) -> BaseGeometry: ...
@overload
def shortest_line(
    a: _ArrayLikeGeometry, b: BaseGeometry | _ArrayLikeGeometry, **kwargs
) -> _NDArrayGeometry: ...
@overload
def shortest_line(
    a: BaseGeometry | _ArrayLikeGeometry, b: _ArrayLikeGeometry, **kwargs
) -> _NDArrayGeometry: ...
