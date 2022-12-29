from typing import overload

from ._typing import (
    _ArrayLikeBool,
    _ArrayLikeFloat,
    _ArrayLikeGeometry,
    _NDArrayGeometry,
)
from .enum import ParamEnum
from .geometry import GeometryCollection, MultiPoint, Point
from .geometry.base import BaseGeometry

class BufferCapStyle(ParamEnum):
    round: int
    flat: int
    square: int

class BufferJoinStyle(ParamEnum):
    round: int
    mitre: int
    bevel: int

@overload
def boundary(geometry: BaseGeometry, **kwargs) -> BaseGeometry: ...
@overload
def boundary(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayGeometry: ...
@overload
def boundary(geometry: None, **kwargs) -> None: ...
@overload
def buffer(
    geometry: BaseGeometry,
    distance: float,
    quad_segs: int = ...,
    cap_style: str = ...,
    join_style: str = ...,
    mitre_limit: float = ...,
    single_sided: bool = ...,
    **kwargs
) -> BaseGeometry: ...
@overload
def buffer(
    geometry: BaseGeometry | _ArrayLikeGeometry,
    distance: _ArrayLikeFloat,
    quad_segs: int = ...,
    cap_style: str = ...,
    join_style: str = ...,
    mitre_limit: float = ...,
    single_sided: bool = ...,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def buffer(
    geometry: _ArrayLikeGeometry,
    distance: float | _ArrayLikeFloat,
    quad_segs: int = ...,
    cap_style: str = ...,
    join_style: str = ...,
    mitre_limit: float = ...,
    single_sided: bool = ...,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def offset_curve(
    geometry: BaseGeometry,
    distance: float,
    quad_segs: int = ...,
    join_style: str = ...,
    mitre_limit: float = ...,
    **kwargs
) -> BaseGeometry: ...
@overload
def offset_curve(
    geometry: BaseGeometry | _ArrayLikeGeometry,
    distance: _ArrayLikeFloat,
    quad_segs: int = ...,
    join_style: str = ...,
    mitre_limit: float = ...,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def offset_curve(
    geometry: _ArrayLikeGeometry,
    distance: float | _ArrayLikeFloat,
    quad_segs: int = ...,
    join_style: str = ...,
    mitre_limit: float = ...,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def centroid(geometry: BaseGeometry, **kwargs) -> Point: ...
@overload
def centroid(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayGeometry: ...
@overload
def clip_by_rect(
    geometry: BaseGeometry, xmin: float, ymin: float, xmax: float, ymax: float, **kwargs
) -> BaseGeometry: ...
@overload
def clip_by_rect(
    geometry: _ArrayLikeGeometry,
    xmin: float,
    ymin: float,
    xmax: float,
    ymax: float,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def concave_hull(
    geometry: BaseGeometry, ratio: float = ..., allow_holes: bool = ..., **kwargs
) -> BaseGeometry: ...
@overload
def concave_hull(
    geometry: _ArrayLikeGeometry, ratio: float = ..., allow_holes: bool = ..., **kwargs
) -> _NDArrayGeometry: ...
@overload
def convex_hull(geometry: BaseGeometry, **kwargs) -> BaseGeometry: ...
@overload
def convex_hull(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayGeometry: ...
@overload
def delaunay_triangles(
    geometry: BaseGeometry, tolerance: float = ..., only_edges: bool = ..., **kwargs
) -> BaseGeometry: ...
@overload
def delaunay_triangles(
    geometry: _ArrayLikeGeometry,
    tolerance: float | _ArrayLikeFloat = ...,
    only_edges: bool = ...,
    **kwargs
) -> _ArrayLikeGeometry: ...
@overload
def delaunay_triangles(
    geometry: BaseGeometry | _ArrayLikeGeometry,
    tolerance: _ArrayLikeFloat,
    only_edges: bool = ...,
    **kwargs
) -> _ArrayLikeGeometry: ...
@overload
def envelope(geometry: BaseGeometry, **kwargs) -> BaseGeometry: ...
@overload
def envelope(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayGeometry: ...
@overload
def extract_unique_points(geometry: BaseGeometry, **kwargs) -> MultiPoint: ...
@overload
def extract_unique_points(geometry: _NDArrayGeometry, **kwargs) -> _NDArrayGeometry: ...
@overload
def build_area(geometry: BaseGeometry, **kwargs) -> BaseGeometry: ...
@overload
def build_area(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayGeometry: ...
@overload
def make_valid(geometry: BaseGeometry, **kwargs) -> BaseGeometry: ...
@overload
def make_valid(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayGeometry: ...
@overload
def normalize(geometry: BaseGeometry, **kwargs) -> BaseGeometry: ...
@overload
def normalize(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayGeometry: ...
@overload
def point_on_surface(geometry: BaseGeometry, **kwargs) -> BaseGeometry: ...
@overload
def point_on_surface(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayGeometry: ...
@overload
def node(geometry: BaseGeometry, **kwargs) -> BaseGeometry: ...
@overload
def node(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayGeometry: ...
def polygonize(
    geometries: _ArrayLikeGeometry, **kwargs
) -> GeometryCollection | _NDArrayGeometry: ...
def polygonize_full(
    geometries: _ArrayLikeGeometry, **kwargs
) -> tuple[
    GeometryCollection, GeometryCollection, GeometryCollection, GeometryCollection
] | tuple[_NDArrayGeometry, _NDArrayGeometry, _NDArrayGeometry, _NDArrayGeometry]: ...
@overload
def remove_repeated_points(
    geometry: BaseGeometry, tolerance: float = ..., **kwargs
) -> BaseGeometry: ...
@overload
def remove_repeated_points(
    geometry: _ArrayLikeGeometry, tolerance: float | _ArrayLikeFloat = ..., **kwargs
) -> _ArrayLikeGeometry: ...
@overload
def remove_repeated_points(
    geometry: BaseGeometry | _ArrayLikeGeometry, tolerance: _ArrayLikeFloat, **kwargs
) -> _ArrayLikeGeometry: ...
@overload
def reverse(geometry: BaseGeometry, **kwargs) -> BaseGeometry: ...
@overload
def reverse(geometry: _ArrayLikeGeometry, **kwargs) -> _ArrayLikeGeometry: ...
def segmentize(geometry, max_segment_length, **kwargs): ...
@overload
def simplify(
    geometry: BaseGeometry, tolerance: float, preserve_topology: bool = ..., **kwargs
) -> BaseGeometry: ...
@overload
def simplify(
    geometry: BaseGeometry | _ArrayLikeGeometry,
    tolerance: _ArrayLikeFloat,
    preserve_topology: bool = ...,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def simplify(
    geometry: _ArrayLikeGeometry,
    tolerance: float | _ArrayLikeFloat,
    preserve_topology: bool = ...,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def snap(
    geometry: BaseGeometry, reference: BaseGeometry, tolerance: float, **kwargs
) -> BaseGeometry: ...
@overload
def snap(
    geometry: _ArrayLikeGeometry,
    reference: BaseGeometry | _ArrayLikeFloat,
    tolerance: float | _ArrayLikeFloat,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def snap(
    geometry: BaseGeometry | _ArrayLikeGeometry,
    reference: _ArrayLikeFloat,
    tolerance: float | _ArrayLikeFloat,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def snap(
    geometry: BaseGeometry | _ArrayLikeGeometry,
    reference: BaseGeometry | _ArrayLikeFloat,
    tolerance: _ArrayLikeFloat,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def voronoi_polygons(
    geometry: BaseGeometry,
    tolerance: float = ...,
    extend_to: BaseGeometry | None = ...,
    only_edges: bool = ...,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def voronoi_polygons(
    geometry: _ArrayLikeGeometry,
    tolerance: float | _ArrayLikeFloat = ...,
    extend_to: BaseGeometry | _ArrayLikeGeometry | None = ...,
    only_edges: bool | _ArrayLikeBool = ...,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def voronoi_polygons(
    geometry: BaseGeometry | _ArrayLikeGeometry,
    tolerance: _ArrayLikeFloat = ...,
    extend_to: BaseGeometry | _ArrayLikeGeometry | None = ...,
    only_edges: bool | _ArrayLikeBool = ...,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def voronoi_polygons(
    geometry: BaseGeometry | _ArrayLikeGeometry,
    tolerance: float | _ArrayLikeFloat = ...,
    extend_to: _ArrayLikeGeometry = ...,
    only_edges: bool | _ArrayLikeBool = ...,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def voronoi_polygons(
    geometry: BaseGeometry | _ArrayLikeGeometry,
    tolerance: float | _ArrayLikeFloat = ...,
    extend_to: BaseGeometry | _ArrayLikeGeometry | None = ...,
    only_edges: _ArrayLikeBool = ...,
    **kwargs
) -> _NDArrayGeometry: ...
@overload
def oriented_envelope(geometry: BaseGeometry, **kwargs) -> BaseGeometry: ...
@overload
def oriented_envelope(geometry: _ArrayLikeGeometry, **kwargs) -> _NDArrayGeometry: ...

minimum_rotated_rectangle = oriented_envelope

@overload
def minimum_bounding_circle(geometry: BaseGeometry, **kwargs) -> BaseGeometry: ...
@overload
def minimum_bounding_circle(
    geometry: _ArrayLikeGeometry, **kwargs
) -> _NDArrayGeometry: ...
