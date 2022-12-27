from _typeshed import Incomplete

from .enum import ParamEnum

class BufferCapStyle(ParamEnum):
    round: int
    flat: int
    square: int

class BufferJoinStyle(ParamEnum):
    round: int
    mitre: int
    bevel: int

def boundary(geometry, **kwargs): ...
def buffer(
    geometry,
    distance,
    quad_segs: int = ...,
    cap_style: str = ...,
    join_style: str = ...,
    mitre_limit: float = ...,
    single_sided: bool = ...,
    **kwargs
): ...
def offset_curve(
    geometry,
    distance,
    quad_segs: int = ...,
    join_style: str = ...,
    mitre_limit: float = ...,
    **kwargs
): ...
def centroid(geometry, **kwargs): ...
def clip_by_rect(geometry, xmin, ymin, xmax, ymax, **kwargs): ...
def concave_hull(geometry, ratio: float = ..., allow_holes: bool = ..., **kwargs): ...
def convex_hull(geometry, **kwargs): ...
def delaunay_triangles(
    geometry, tolerance: float = ..., only_edges: bool = ..., **kwargs
): ...
def envelope(geometry, **kwargs): ...
def extract_unique_points(geometry, **kwargs): ...
def build_area(geometry, **kwargs): ...
def make_valid(geometry, **kwargs): ...
def normalize(geometry, **kwargs): ...
def point_on_surface(geometry, **kwargs): ...
def node(geometry, **kwargs): ...
def polygonize(geometries, **kwargs): ...
def polygonize_full(geometries, **kwargs): ...
def remove_repeated_points(geometry, tolerance: float = ..., **kwargs): ...
def reverse(geometry, **kwargs): ...
def segmentize(geometry, max_segment_length, **kwargs): ...
def simplify(geometry, tolerance, preserve_topology: bool = ..., **kwargs): ...
def snap(geometry, reference, tolerance, **kwargs): ...
def voronoi_polygons(
    geometry,
    tolerance: float = ...,
    extend_to: Incomplete | None = ...,
    only_edges: bool = ...,
    **kwargs
): ...
def oriented_envelope(geometry, **kwargs): ...

minimum_rotated_rectangle = oriented_envelope

def minimum_bounding_circle(geometry, **kwargs): ...
