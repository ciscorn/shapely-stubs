from typing import Literal, overload

from numpy import ufunc

from ._typing import _NDArrayFloat, _NDArrayGeometry, _NDArrayInt
from .geometry.base import BaseGeometry

class Geometry: ...
class ShapelyError(Exception): ...
class GEOSException(ShapelyError): ...
class STRtree: ...

geos_capi_version: tuple[int, int, int]
geos_capi_version_string: str
geos_version: tuple[int, int, int]
geos_version_string: str

registry: list[BaseGeometry]

def count_coordinates(_a: _NDArrayGeometry) -> int: ...
@overload
def get_coordinates(
    _a: _NDArrayGeometry, include_z: bool, return_index: Literal[False]
) -> _NDArrayFloat: ...
@overload
def get_coordinates(
    _a: _NDArrayGeometry, include_z: bool, return_index: Literal[True]
) -> tuple[_NDArrayFloat, _NDArrayInt]: ...
def set_coordinates(_a: _NDArrayGeometry, _c: _NDArrayFloat) -> _NDArrayGeometry: ...

area: ufunc
boundary: ufunc
bounds: ufunc
box: ufunc
buffer: ufunc
build_area: ufunc
centroid: ufunc
clip_by_rect: ufunc
concave_hull: ufunc
contains: ufunc
contains_properly: ufunc
contains_xy: ufunc
convex_hull: ufunc
coverage_union: ufunc
covered_by: ufunc
covers: ufunc
create_collection: ufunc
crosses: ufunc
delaunay_triangles: ufunc
destroy_prepared: ufunc
difference: ufunc
difference_prec: ufunc
disjoint: ufunc
distance: ufunc
dwithin: ufunc
envelope: ufunc
equals: ufunc
equals_exact: ufunc
extract_unique_points: ufunc
force_2d: ufunc
force_3d: ufunc
frechet_distance: ufunc
frechet_distance_densify: ufunc
from_geojson: ufunc
from_wkb: ufunc
from_wkt: ufunc
get_coordinate_dimension: ufunc
get_dimensions: ufunc
get_exterior_ring: ufunc
get_geometry: ufunc
get_interior_ring: ufunc
get_num_coordinates: ufunc
get_num_geometries: ufunc
get_num_interior_rings: ufunc
get_num_points: ufunc
get_point: ufunc
get_precision: ufunc
get_srid: ufunc
get_type_id: ufunc
get_x: ufunc
get_y: ufunc
get_z: ufunc
has_z: ufunc
hausdorff_distance: ufunc
hausdorff_distance_densify: ufunc
intersection: ufunc
intersection_all: ufunc
intersection_prec: ufunc
intersects: ufunc
intersects_xy: ufunc
is_ccw: ufunc
is_closed: ufunc
is_empty: ufunc
is_geometry: ufunc
is_missing: ufunc
is_prepared: ufunc
is_ring: ufunc
is_simple: ufunc
is_valid: ufunc
is_valid_input: ufunc
is_valid_reason: ufunc
length: ufunc
line_interpolate_point: ufunc
line_interpolate_point_normalized: ufunc
line_locate_point: ufunc
line_locate_point_normalized: ufunc
line_merge: ufunc
line_merge_directed: ufunc
linearrings: ufunc
linestrings: ufunc
make_valid: ufunc
minimum_bounding_circle: ufunc
minimum_bounding_radius: ufunc
minimum_clearance: ufunc
node: ufunc
normalize: ufunc
offset_curve: ufunc
oriented_envelope: ufunc
overlaps: ufunc
point_on_surface: ufunc
points: ufunc
polygonize: ufunc
polygonize_full: ufunc
polygons: ufunc
prepare: ufunc
relate: ufunc
relate_pattern: ufunc
remove_repeated_points: ufunc
reverse: ufunc
segmentize: ufunc
set_precision: ufunc
set_srid: ufunc
shared_paths: ufunc
shortest_line: ufunc
simplify: ufunc
simplify_preserve_topology: ufunc
snap: ufunc
symmetric_difference: ufunc
symmetric_difference_all: ufunc
symmetric_difference_prec: ufunc
to_geojson: ufunc
to_wkb: ufunc
to_wkt: ufunc
touches: ufunc
unary_union: ufunc
unary_union_prec: ufunc
union: ufunc
union_prec: ufunc
voronoi_polygons: ufunc
within: ufunc
