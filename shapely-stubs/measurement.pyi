from typing import overload

import numpy

from ._typing import _ArrayLikeFloat, _ArrayLikeGeometry, _NDArrayFloat
from .geometry.base import BaseGeometry

@overload
def area(geometry: BaseGeometry | None, **kwargs) -> numpy.float64: ...
@overload
def area(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayFloat: ...
@overload
def distance(
    a: BaseGeometry | None, b: BaseGeometry | None, **kwargs
) -> numpy.float64: ...
@overload
def distance(
    a: _ArrayLikeGeometry, b: BaseGeometry | _ArrayLikeGeometry | None, **kwargs
) -> _NDArrayFloat: ...
@overload
def distance(
    a: BaseGeometry | _ArrayLikeGeometry | None, b: _ArrayLikeGeometry, **kwargs
) -> _NDArrayFloat: ...
def bounds(
    geometry: BaseGeometry | _ArrayLikeGeometry | None, **kwargs
) -> _NDArrayFloat: ...
def total_bounds(
    geometry: BaseGeometry | _ArrayLikeGeometry | None, **kwargs
) -> _NDArrayFloat: ...
@overload
def length(geometry: BaseGeometry | None, **kwargs) -> numpy.float64: ...
@overload
def length(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayFloat: ...
@overload
def hausdorff_distance(
    a: BaseGeometry | None,
    b: BaseGeometry | None,
    densify: float | None = ...,
    **kwargs
) -> numpy.float64: ...
@overload
def hausdorff_distance(
    a: _ArrayLikeGeometry,
    b: BaseGeometry | _ArrayLikeGeometry | None,
    densify: float | _ArrayLikeFloat | None = ...,
    **kwargs
) -> _NDArrayFloat: ...
@overload
def hausdorff_distance(
    a: BaseGeometry | _ArrayLikeGeometry | None,
    b: _ArrayLikeGeometry,
    densify: float | _ArrayLikeFloat | None = ...,
    **kwargs
) -> _NDArrayFloat: ...
@overload
def hausdorff_distance(
    a: BaseGeometry | _ArrayLikeGeometry | None,
    b: BaseGeometry | _ArrayLikeGeometry | None,
    densify: _ArrayLikeFloat,
    **kwargs
) -> _NDArrayFloat: ...
@overload
def frechet_distance(
    a: BaseGeometry | None,
    b: BaseGeometry | None,
    densify: float | None = ...,
    **kwargs
) -> numpy.float64: ...
@overload
def frechet_distance(
    a: _ArrayLikeGeometry,
    b: BaseGeometry | _ArrayLikeGeometry | None,
    densify: float | _ArrayLikeFloat | None = ...,
    **kwargs
) -> _NDArrayFloat: ...
@overload
def frechet_distance(
    a: BaseGeometry | _ArrayLikeGeometry | None,
    b: _ArrayLikeGeometry,
    densify: float | _ArrayLikeFloat | None = ...,
    **kwargs
) -> _NDArrayFloat: ...
@overload
def frechet_distance(
    a: BaseGeometry | _ArrayLikeGeometry | None,
    b: BaseGeometry | _ArrayLikeGeometry | None,
    densify: _ArrayLikeFloat,
    **kwargs
) -> _NDArrayFloat: ...
@overload
def minimum_clearance(geometry: BaseGeometry | None, **kwargs) -> numpy.float64: ...
@overload
def minimum_clearance(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayFloat: ...
@overload
def minimum_bounding_radius(
    geometry: BaseGeometry | None, **kwargs
) -> numpy.float64: ...
@overload
def minimum_bounding_radius(
    geometry: _ArrayLikeGeometry, **kwargs
) -> _NDArrayFloat: ...
