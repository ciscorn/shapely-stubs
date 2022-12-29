from typing import Iterable

from shapely import GeometryType
from shapely._typing import _ArrayLikeGeometry, _NDArrayFloat, _NDArrayGeometry

def to_ragged_array(
    geometries: _ArrayLikeGeometry, include_z: bool | None = ...
) -> tuple[GeometryType, _NDArrayFloat, tuple[_NDArrayFloat, ...]]: ...
def from_ragged_array(
    geometry_type: GeometryType,
    coords: _NDArrayFloat,
    offsets: Iterable[_NDArrayFloat] | None = ...,
) -> _NDArrayGeometry: ...
