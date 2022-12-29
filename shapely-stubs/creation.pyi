from typing import Literal, overload

from shapely import GeometryType
from shapely.geometry import (
    GeometryCollection,
    LinearRing,
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)
from shapely.geometry.base import BaseGeometry

from ._typing import (
    _ArrayLikeFloat,
    _ArrayLikeGeometry,
    _ArrayLikeInt,
    _NDArrayGeometry,
)

def points(
    coords: _ArrayLikeFloat,
    y: _ArrayLikeFloat | None = ...,
    z: _ArrayLikeFloat | None = ...,
    indices: _ArrayLikeInt | None = ...,
    out: _NDArrayGeometry | None = ...,
    **kwargs
) -> Point | _NDArrayGeometry: ...
def linestrings(
    coords: _ArrayLikeFloat,
    y: _ArrayLikeFloat | None = ...,
    z: _ArrayLikeFloat | None = ...,
    indices: _ArrayLikeInt | None = ...,
    out: _NDArrayGeometry | None = ...,
    **kwargs
) -> LineString | _NDArrayGeometry: ...
def linearrings(
    coords: _ArrayLikeFloat,
    y: _ArrayLikeFloat | None = ...,
    z: _ArrayLikeFloat | None = ...,
    indices: _ArrayLikeInt | None = ...,
    out: _NDArrayGeometry | None = ...,
    **kwargs
) -> LinearRing | _NDArrayGeometry: ...
def polygons(
    geometries: _ArrayLikeGeometry | _ArrayLikeFloat | None,
    holes: _ArrayLikeGeometry | _ArrayLikeFloat | None = ...,
    indices: _ArrayLikeInt | None = ...,
    out: _NDArrayGeometry | None = ...,
    **kwargs
) -> Polygon | _NDArrayGeometry: ...
@overload
def box(
    xmin: float, ymin: float, xmax: float, ymax: float, ccw: bool = ..., **kwargs
) -> Polygon: ...
@overload
def box(
    xmin: _ArrayLikeFloat,
    ymin: float | _ArrayLikeFloat,
    xmax: float | _ArrayLikeFloat,
    ymax: float | _ArrayLikeFloat,
    ccw: bool = ...,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def box(
    xmin: float | _ArrayLikeFloat,
    ymin: _ArrayLikeFloat,
    xmax: float | _ArrayLikeFloat,
    ymax: float | _ArrayLikeFloat,
    ccw: bool = ...,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def box(
    xmin: float | _ArrayLikeFloat,
    ymin: float | _ArrayLikeFloat,
    xmax: _ArrayLikeFloat,
    ymax: float | _ArrayLikeFloat,
    ccw: bool = ...,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def box(
    xmin: float | _ArrayLikeFloat,
    ymin: float | _ArrayLikeFloat,
    xmax: float | _ArrayLikeFloat,
    ymax: _ArrayLikeFloat,
    ccw: bool = ...,
    **kwargs
) -> _NDArrayGeometry: ...
def multipoints(
    geometries: _ArrayLikeGeometry | _ArrayLikeFloat,
    indices: _ArrayLikeInt | None = ...,
    out: _NDArrayGeometry | None = ...,
    **kwargs
) -> MultiPoint | _NDArrayGeometry: ...
def multilinestrings(
    geometries: _ArrayLikeGeometry | _ArrayLikeFloat,
    indices: _ArrayLikeInt | None = ...,
    out: _NDArrayGeometry | None = ...,
    **kwargs
) -> MultiLineString | _NDArrayGeometry: ...
def multipolygons(
    geometries: _ArrayLikeGeometry | _ArrayLikeFloat,
    indices: _ArrayLikeInt | None = ...,
    out: _NDArrayGeometry | None = ...,
    **kwargs
) -> MultiPolygon | _NDArrayGeometry: ...
def geometrycollections(
    geometries: _ArrayLikeGeometry | _ArrayLikeFloat,
    indices: _ArrayLikeInt | None = ...,
    out: _NDArrayGeometry | None = ...,
    **kwargs
) -> GeometryCollection | _NDArrayGeometry: ...
def prepare(geometry: BaseGeometry | _ArrayLikeGeometry | None, **kwargs) -> None: ...
def destroy_prepared(
    geometry: BaseGeometry | _ArrayLikeGeometry | None, **kwargs
) -> None: ...
def empty(
    shape: int | _ArrayLikeInt,
    geom_type: GeometryType | None = ...,
    order: Literal["C", "F"] = ...,
) -> _NDArrayGeometry: ...
