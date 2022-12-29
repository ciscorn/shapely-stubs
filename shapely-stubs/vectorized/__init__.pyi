from typing import overload

import numpy
from shapely.prepared import PreparedGeometry as PreparedGeometry

from .._typing import _ArrayLikeFloat, _ArrayLikeGeometry, _NDArrayBool
from ..geometry.base import BaseGeometry

@overload
def contains(geometry: BaseGeometry, x: float, y: float) -> numpy.bool_: ...
@overload
def contains(
    geometry: _ArrayLikeGeometry, x: float | _ArrayLikeFloat, y: float | _ArrayLikeFloat
) -> _NDArrayBool: ...
@overload
def contains(
    geometry: BaseGeometry | _ArrayLikeGeometry,
    x: _ArrayLikeFloat,
    y: float | _ArrayLikeFloat,
) -> _NDArrayBool: ...
@overload
def contains(
    geometry: BaseGeometry | _ArrayLikeGeometry,
    x: float | _ArrayLikeFloat,
    y: _ArrayLikeFloat,
) -> _NDArrayBool: ...
@overload
def touches(geometry: BaseGeometry, x: float, y: float) -> numpy.bool_: ...
@overload
def touches(
    geometry: _ArrayLikeGeometry, x: float | _ArrayLikeFloat, y: float | _ArrayLikeFloat
) -> _NDArrayBool: ...
@overload
def touches(
    geometry: BaseGeometry | _ArrayLikeGeometry,
    x: _ArrayLikeFloat,
    y: float | _ArrayLikeFloat,
) -> _NDArrayBool: ...
@overload
def touches(
    geometry: BaseGeometry | _ArrayLikeGeometry,
    x: float | _ArrayLikeFloat,
    y: _ArrayLikeFloat,
) -> _NDArrayBool: ...
