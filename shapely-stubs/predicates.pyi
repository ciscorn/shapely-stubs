from typing import overload

import numpy

from ._typing import (
    _ArrayLikeFloat,
    _ArrayLikeGeometry,
    _ArrayLikeObject,
    _NDArrayBool,
    _NDArrayObject,
)
from .geometry.base import BaseGeometry

@overload
def has_z(geometry: BaseGeometry | None, **kwargs) -> numpy.bool_: ...
@overload
def has_z(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayBool: ...
@overload
def is_ccw(geometry: BaseGeometry | None, **kwargs) -> numpy.bool_: ...
@overload
def is_ccw(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayBool: ...
@overload
def is_closed(geometry: BaseGeometry | None, **kwargs) -> numpy.bool_: ...
@overload
def is_closed(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayBool: ...
@overload
def is_empty(geometry: BaseGeometry | None, **kwargs) -> numpy.bool_: ...
@overload
def is_empty(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayBool: ...
@overload
def is_geometry(geometry: BaseGeometry | None, **kwargs) -> numpy.bool_: ...
@overload
def is_geometry(geometry: _ArrayLikeObject, **kwargs) -> _NDArrayBool: ...
@overload
def is_geometry(
    geometry: object | _ArrayLikeObject, **kwargs
) -> numpy.bool_ | _NDArrayBool: ...
@overload
def is_missing(geometry: BaseGeometry | None, **kwargs) -> numpy.bool_: ...
@overload
def is_missing(geometry: _ArrayLikeObject, **kwargs) -> _NDArrayBool: ...
@overload
def is_missing(
    geometry: object | _ArrayLikeObject, **kwargs
) -> numpy.bool_ | _NDArrayBool: ...
@overload
def is_prepared(geometry: BaseGeometry | None, **kwargs) -> numpy.bool_: ...
@overload
def is_prepared(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayBool: ...
@overload
def is_valid_input(geometry: BaseGeometry | None, **kwargs) -> numpy.bool_: ...
@overload
def is_valid_input(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayBool: ...
@overload
def is_ring(geometry: BaseGeometry | None, **kwargs) -> numpy.bool_: ...
@overload
def is_ring(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayBool: ...
@overload
def is_simple(geometry: BaseGeometry | None, **kwargs) -> numpy.bool_: ...
@overload
def is_simple(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayBool: ...
@overload
def is_valid(geometry: BaseGeometry | None, **kwargs) -> numpy.bool_: ...
@overload
def is_valid(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayBool: ...
@overload
def is_valid_reason(geometry: BaseGeometry, **kwargs) -> str: ...
@overload
def is_valid_reason(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayObject: ...
@overload
def is_valid_reason(geometry: None, **kwargs) -> None: ...
@overload
def crosses(
    a: BaseGeometry | None, b: BaseGeometry | None, **kwargs
) -> numpy.bool_: ...
@overload
def crosses(
    a: BaseGeometry | _ArrayLikeGeometry | None, b: _ArrayLikeGeometry, **kwargs
) -> _NDArrayBool: ...
@overload
def crosses(
    a: _ArrayLikeGeometry, b: BaseGeometry | _ArrayLikeGeometry | None, **kwargs
) -> _NDArrayBool: ...
@overload
def contains(
    a: BaseGeometry | None, b: BaseGeometry | None, **kwargs
) -> numpy.bool_: ...
@overload
def contains(
    a: BaseGeometry | _ArrayLikeGeometry | None, b: _ArrayLikeGeometry, **kwargs
) -> _NDArrayBool: ...
@overload
def contains(
    a: _ArrayLikeGeometry, b: BaseGeometry | _ArrayLikeGeometry | None, **kwargs
) -> _NDArrayBool: ...
@overload
def contains_properly(
    a: BaseGeometry | None, b: BaseGeometry | None, **kwargs
) -> numpy.bool_: ...
@overload
def contains_properly(
    a: BaseGeometry | _ArrayLikeGeometry | None, b: _ArrayLikeGeometry, **kwargs
) -> _NDArrayBool: ...
@overload
def contains_properly(
    a: _ArrayLikeGeometry, b: BaseGeometry | _ArrayLikeGeometry | None, **kwargs
) -> _NDArrayBool: ...
@overload
def covered_by(
    a: BaseGeometry | None, b: BaseGeometry | None, **kwargs
) -> numpy.bool_: ...
@overload
def covered_by(
    a: BaseGeometry | _ArrayLikeGeometry | None, b: _ArrayLikeGeometry, **kwargs
) -> _NDArrayBool: ...
@overload
def covered_by(
    a: _ArrayLikeGeometry, b: BaseGeometry | _ArrayLikeGeometry | None, **kwargs
) -> _NDArrayBool: ...
@overload
def covers(a: BaseGeometry | None, b: BaseGeometry | None, **kwargs) -> numpy.bool_: ...
@overload
def covers(
    a: BaseGeometry | _ArrayLikeGeometry | None, b: _ArrayLikeGeometry, **kwargs
) -> _NDArrayBool: ...
@overload
def covers(
    a: _ArrayLikeGeometry, b: BaseGeometry | _ArrayLikeGeometry | None, **kwargs
) -> _NDArrayBool: ...
@overload
def disjoint(
    a: BaseGeometry | None, b: BaseGeometry | None, **kwargs
) -> numpy.bool_: ...
@overload
def disjoint(
    a: BaseGeometry | _ArrayLikeGeometry | None, b: _ArrayLikeGeometry, **kwargs
) -> _NDArrayBool: ...
@overload
def disjoint(
    a: _ArrayLikeGeometry, b: BaseGeometry | _ArrayLikeGeometry | None, **kwargs
) -> _NDArrayBool: ...
@overload
def equals(a: BaseGeometry | None, b: BaseGeometry | None, **kwargs) -> numpy.bool_: ...
@overload
def equals(
    a: BaseGeometry | _ArrayLikeGeometry | None, b: _ArrayLikeGeometry, **kwargs
) -> _NDArrayBool: ...
@overload
def equals(
    a: _ArrayLikeGeometry, b: BaseGeometry | _ArrayLikeGeometry | None, **kwargs
) -> _NDArrayBool: ...
@overload
def intersects(
    a: BaseGeometry | None, b: BaseGeometry | None, **kwargs
) -> numpy.bool_: ...
@overload
def intersects(
    a: BaseGeometry | _ArrayLikeGeometry | None, b: _ArrayLikeGeometry, **kwargs
) -> _NDArrayBool: ...
@overload
def intersects(
    a: _ArrayLikeGeometry, b: BaseGeometry | _ArrayLikeGeometry | None, **kwargs
) -> _NDArrayBool: ...
@overload
def overlaps(
    a: BaseGeometry | None, b: BaseGeometry | None, **kwargs
) -> numpy.bool_: ...
@overload
def overlaps(
    a: BaseGeometry | _ArrayLikeGeometry | None, b: _ArrayLikeGeometry, **kwargs
) -> _NDArrayBool: ...
@overload
def overlaps(
    a: _ArrayLikeGeometry, b: BaseGeometry | _ArrayLikeGeometry | None, **kwargs
) -> _NDArrayBool: ...
@overload
def touches(
    a: BaseGeometry | None, b: BaseGeometry | None, **kwargs
) -> numpy.bool_: ...
@overload
def touches(
    a: BaseGeometry | _ArrayLikeGeometry | None, b: _ArrayLikeGeometry, **kwargs
) -> _NDArrayBool: ...
@overload
def touches(
    a: _ArrayLikeGeometry, b: BaseGeometry | _ArrayLikeGeometry | None, **kwargs
) -> _NDArrayBool: ...
@overload
def within(a: BaseGeometry | None, b: BaseGeometry | None, **kwargs) -> numpy.bool_: ...
@overload
def within(
    a: BaseGeometry | _ArrayLikeGeometry | None, b: _ArrayLikeGeometry, **kwargs
) -> _NDArrayBool: ...
@overload
def within(
    a: _ArrayLikeGeometry, b: BaseGeometry | _ArrayLikeGeometry | None, **kwargs
) -> _NDArrayBool: ...
@overload
def equals_exact(
    a: BaseGeometry | None, b: BaseGeometry | None, tolerance: float = ..., **kwargs
) -> numpy.bool_: ...
@overload
def equals_exact(
    a: BaseGeometry | _ArrayLikeGeometry | None,
    b: _ArrayLikeGeometry,
    tolerance: float | _ArrayLikeFloat = ...,
    **kwargs
) -> _NDArrayBool: ...
@overload
def equals_exact(
    a: _ArrayLikeGeometry,
    b: BaseGeometry | _ArrayLikeGeometry | None,
    tolerance: float | _ArrayLikeFloat = ...,
    **kwargs
) -> _NDArrayBool: ...
@overload
def equals_exact(
    a: BaseGeometry | _ArrayLikeGeometry | None,
    b: BaseGeometry | _ArrayLikeGeometry | None,
    tolerance: _ArrayLikeFloat,
    **kwargs
) -> _NDArrayBool: ...
@overload
def relate(a: BaseGeometry, b: BaseGeometry, **kwargs) -> str: ...
@overload
def relate(
    a: BaseGeometry | _ArrayLikeGeometry | None, b: _ArrayLikeGeometry, **kwargs
) -> _NDArrayObject: ...
@overload
def relate(
    a: _ArrayLikeGeometry, b: BaseGeometry | _ArrayLikeGeometry | None, **kwargs
) -> _NDArrayObject: ...
@overload
def relate(a: None, b: BaseGeometry | None, **kwargs) -> None: ...
@overload
def relate(a: BaseGeometry | None, b: None, **kwargs) -> None: ...
@overload
def relate_pattern(
    a: BaseGeometry | None, b: BaseGeometry | None, pattern: str, **kwargs
) -> numpy.bool_: ...
@overload
def relate_pattern(
    a: BaseGeometry | _ArrayLikeGeometry | None,
    b: _ArrayLikeGeometry,
    pattern: str,
    **kwargs
) -> _NDArrayBool: ...
@overload
def relate_pattern(
    a: _ArrayLikeGeometry,
    b: BaseGeometry | _ArrayLikeGeometry | None,
    pattern: str,
    **kwargs
) -> _NDArrayBool: ...
@overload
def dwithin(
    a: BaseGeometry | None, b: BaseGeometry | None, distance: float = ..., **kwargs
) -> numpy.bool_: ...
@overload
def dwithin(
    a: BaseGeometry | _ArrayLikeGeometry | None,
    b: _ArrayLikeGeometry,
    distance: float | _ArrayLikeFloat = ...,
    **kwargs
) -> _NDArrayBool: ...
@overload
def dwithin(
    a: _ArrayLikeGeometry,
    b: BaseGeometry | _ArrayLikeGeometry | None,
    distance: float | _ArrayLikeFloat = ...,
    **kwargs
) -> _NDArrayBool: ...
@overload
def dwithin(
    a: BaseGeometry | _ArrayLikeGeometry | None,
    b: BaseGeometry | _ArrayLikeGeometry | None,
    distance: _ArrayLikeFloat,
    **kwargs
) -> _NDArrayBool: ...
@overload
def contains_xy(
    geom: BaseGeometry | None, x: float, y: float | None = ..., **kwargs
) -> numpy.bool_: ...
@overload
def contains_xy(
    geom: _ArrayLikeGeometry,
    x: float | _ArrayLikeFloat,
    y: float | _ArrayLikeFloat | None = ...,
    **kwargs
) -> _NDArrayBool: ...
@overload
def contains_xy(
    geom: BaseGeometry | _ArrayLikeGeometry | None,
    x: _ArrayLikeFloat,
    y: float | _ArrayLikeFloat | None = ...,
    **kwargs
) -> _NDArrayBool: ...
@overload
def contains_xy(
    geom: BaseGeometry | _ArrayLikeGeometry | None,
    x: float | _ArrayLikeFloat,
    y: _ArrayLikeFloat,
    **kwargs
) -> _NDArrayBool: ...
@overload
def intersects_xy(
    geom: BaseGeometry | None, x: float, y: float | None = ..., **kwargs
) -> numpy.bool_: ...
@overload
def intersects_xy(
    geom: _ArrayLikeGeometry,
    x: float | _ArrayLikeFloat,
    y: float | _ArrayLikeFloat | None = ...,
    **kwargs
) -> _NDArrayBool: ...
@overload
def intersects_xy(
    geom: BaseGeometry | _ArrayLikeGeometry | None,
    x: _ArrayLikeFloat,
    y: float | _ArrayLikeFloat | None = ...,
    **kwargs
) -> _NDArrayBool: ...
@overload
def intersects_xy(
    geom: BaseGeometry | _ArrayLikeGeometry | None,
    x: float | _ArrayLikeFloat,
    y: _ArrayLikeFloat,
    **kwargs
) -> _NDArrayBool: ...
