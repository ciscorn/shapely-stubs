from enum import IntEnum
from typing import Literal, overload

import numpy
from numpy.typing import NDArray

from ._typing import (
    _ArrayLikeGeometry,
    _ArrayLikeInt,
    _NDArrayFloat,
    _NDArrayGeometry,
    _NDArrayInt,
)
from .enum import ParamEnum
from .geometry.base import BaseGeometry
from .geometry.point import Point

class GeometryType(IntEnum):
    MISSING: int
    POINT: int
    LINESTRING: int
    LINEARRING: int
    POLYGON: int
    MULTIPOINT: int
    MULTILINESTRING: int
    MULTIPOLYGON: int
    GEOMETRYCOLLECTION: int

@overload
def get_type_id(geometry: BaseGeometry | None, **kwargs) -> numpy.int32: ...
@overload
def get_type_id(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayInt: ...
@overload
def get_dimensions(geometry: BaseGeometry | None, **kwargs) -> numpy.int32: ...
@overload
def get_dimensions(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayInt: ...
@overload
def get_coordinate_dimension(
    geometry: BaseGeometry | None, **kwargs
) -> numpy.int32: ...
@overload
def get_coordinate_dimension(geometry: _ArrayLikeGeometry, **kwargs) -> numpy.int32: ...
@overload
def get_num_coordinates(geometry: BaseGeometry | None, **kwargs) -> numpy.int32: ...
@overload
def get_num_coordinates(geometry: _ArrayLikeGeometry, **kwargs) -> numpy.int32: ...
@overload
def get_srid(geometry: BaseGeometry | None, srid: int, **kwargs) -> numpy.int32: ...
@overload
def get_srid(
    geometry: _ArrayLikeGeometry, srid: int, **kwargs
) -> NDArray[numpy.int32]: ...
@overload
def set_srid(geometry: BaseGeometry, srid: int, **kwargs) -> BaseGeometry: ...
@overload
def set_srid(
    geometry: _ArrayLikeGeometry, srid: int, **kwargs
) -> _ArrayLikeGeometry: ...
@overload
def set_srid(geometry: None, srid: int, **kwargs) -> None: ...
@overload
def get_x(point: BaseGeometry | None, **kwargs) -> numpy.float64: ...
@overload
def get_x(point: _ArrayLikeGeometry, **kwargs) -> _NDArrayFloat: ...
@overload
def get_y(point: BaseGeometry | None, **kwargs) -> numpy.float64: ...
@overload
def get_y(point: _ArrayLikeGeometry, **kwargs) -> _NDArrayFloat: ...
@overload
def get_z(point: BaseGeometry | None, **kwargs) -> numpy.float64: ...
@overload
def get_z(point: _ArrayLikeGeometry, **kwargs) -> _NDArrayFloat: ...
@overload
def get_point(geometry: BaseGeometry | None, index: int, **kwargs) -> Point | None: ...
@overload
def get_point(
    geometry: BaseGeometry | _ArrayLikeGeometry | None, index: _ArrayLikeInt, **kwargs
) -> _NDArrayGeometry: ...
@overload
def get_point(
    geometry: _ArrayLikeGeometry, index: int | _ArrayLikeInt, **kwargs
) -> _NDArrayGeometry: ...
@overload
def get_num_points(geometry: BaseGeometry | None, **kwargs) -> numpy.int32: ...
@overload
def get_num_points(geometry: _ArrayLikeGeometry, **kwargs) -> NDArray[numpy.int32]: ...
@overload
def get_exterior_ring(
    geometry: BaseGeometry | None, **kwargs
) -> BaseGeometry | None: ...
@overload
def get_exterior_ring(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayGeometry: ...
@overload
def get_interior_ring(
    geometry: BaseGeometry | None, index: int, **kwargs
) -> BaseGeometry | None: ...
@overload
def get_interior_ring(
    geometry: BaseGeometry | _ArrayLikeGeometry | None, index: _ArrayLikeInt, **kwargs
) -> _NDArrayGeometry: ...
@overload
def get_interior_ring(
    geometry: _ArrayLikeGeometry, index: int | _ArrayLikeInt, **kwargs
) -> _NDArrayGeometry: ...
@overload
def get_num_interior_rings(geometry: BaseGeometry | None, **kwargs) -> numpy.int32: ...
@overload
def get_num_interior_rings(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayInt: ...
@overload
def get_geometry(
    geometry: BaseGeometry | None, index: int, **kwargs
) -> BaseGeometry | None: ...
@overload
def get_geometry(
    geometry: BaseGeometry | _ArrayLikeGeometry | None, index: _ArrayLikeInt, **kwargs
) -> _NDArrayGeometry: ...
@overload
def get_geometry(
    geometry: _ArrayLikeGeometry, index: int | _ArrayLikeInt, **kwargs
) -> _NDArrayGeometry: ...
@overload
def get_parts(
    geometry: BaseGeometry | _ArrayLikeGeometry | None,
    return_index: Literal[False] = ...,
) -> _NDArrayGeometry: ...
@overload
def get_parts(
    geometry: BaseGeometry | _ArrayLikeGeometry | None, return_index: Literal[True]
) -> tuple[_NDArrayGeometry, _NDArrayInt]: ...
@overload
def get_rings(
    geometry: BaseGeometry | _ArrayLikeGeometry | None,
    return_index: Literal[False] = ...,
) -> _NDArrayGeometry: ...
@overload
def get_rings(
    geometry: BaseGeometry | _ArrayLikeGeometry | None, return_index: Literal[True]
) -> tuple[_NDArrayGeometry, _NDArrayInt]: ...
@overload
def get_num_geometries(geometry: BaseGeometry | None, **kwargs) -> numpy.int32: ...
@overload
def get_num_geometries(geometry: _ArrayLikeGeometry, **kwargs) -> numpy.int32: ...
@overload
def get_precision(geometry: BaseGeometry | None, **kwargs) -> numpy.float64: ...
@overload
def get_precision(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayFloat: ...

class SetPrecisionMode(ParamEnum):
    valid_output: int
    pointwise: int
    keep_collapsed: int

@overload
def set_precision(
    geometry: BaseGeometry,
    grid_size: float,
    mode: str | SetPrecisionMode = ...,
    **kwargs
) -> BaseGeometry: ...
@overload
def set_precision(
    geometry: _ArrayLikeGeometry,
    grid_size: float | _NDArrayFloat,
    mode: str | SetPrecisionMode = ...,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def set_precision(
    geometry: BaseGeometry | _ArrayLikeGeometry,
    grid_size: _NDArrayFloat,
    mode: str | SetPrecisionMode = ...,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def set_precision(
    geometry: None,
    grid_size: float | _NDArrayFloat,
    mode: str | SetPrecisionMode = ...,
    **kwargs
) -> None: ...
@overload
def force_2d(geometry: BaseGeometry, **kwargs) -> BaseGeometry: ...
@overload
def force_2d(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayGeometry: ...
@overload
def force_2d(geometry: None, **kwargs) -> None: ...
@overload
def force_3d(geometry: BaseGeometry, z: float = ..., **kwargs) -> BaseGeometry: ...
@overload
def force_3d(
    geometry: _ArrayLikeGeometry, z: float | _ArrayLikeGeometry = ..., **kwargs
) -> _ArrayLikeGeometry: ...
@overload
def force_3d(
    geometry: BaseGeometry | _ArrayLikeGeometry, z: _ArrayLikeGeometry, **kwargs
) -> _ArrayLikeGeometry: ...
@overload
def force_3d(geometry: None, z: float | _ArrayLikeGeometry = ..., **kwargs) -> None: ...
