from typing import AnyStr, overload

from ._ragged_array import from_ragged_array as from_ragged_array
from ._ragged_array import to_ragged_array as to_ragged_array
from ._typing import (
    _ArrayLikeAnyStr,
    _ArrayLikeGeometry,
    _NDArrayGeometry,
    _NDArrayObject,
)
from .geometry.base import BaseGeometry

@overload
def to_wkt(
    geometry: BaseGeometry,
    rounding_precision: int = ...,
    trim: bool = ...,
    output_dimension: int = ...,
    old_3d: bool = ...,
    **kwargs
) -> str: ...
@overload
def to_wkt(
    geometry: _ArrayLikeGeometry,
    rounding_precision: int = ...,
    trim: bool = ...,
    output_dimension: int = ...,
    old_3d: bool = ...,
    **kwargs
) -> _NDArrayObject: ...
@overload
def to_wkt(
    geometry: None,
    rounding_precision: int = ...,
    trim: bool = ...,
    output_dimension: int = ...,
    old_3d: bool = ...,
    **kwargs
) -> None: ...
@overload
def to_wkb(
    geometry: BaseGeometry,
    hex: bool = ...,
    output_dimension: int = ...,
    byte_order: int = ...,
    include_srid: bool = ...,
    flavor: str = ...,
    **kwargs
) -> bytes: ...
@overload
def to_wkb(
    geometry: _ArrayLikeGeometry,
    hex: bool = ...,
    output_dimension: int = ...,
    byte_order: int = ...,
    include_srid: bool = ...,
    flavor: str = ...,
    **kwargs
) -> _NDArrayObject: ...
@overload
def to_wkb(
    geometry: None,
    hex: bool = ...,
    output_dimension: int = ...,
    byte_order: int = ...,
    include_srid: bool = ...,
    flavor: str = ...,
    **kwargs
) -> None: ...
@overload
def to_geojson(geometry: BaseGeometry, indent: int | None = ..., **kwargs) -> str: ...
@overload
def to_geojson(
    geometry: _ArrayLikeGeometry, indent: int | None = ..., **kwargs
) -> _NDArrayObject: ...
@overload
def to_geojson(geometry: None, indent: int | None = ..., **kwargs) -> None: ...
@overload
def from_wkt(geometry: AnyStr, on_invalid: str = ..., **kwargs) -> BaseGeometry: ...
@overload
def from_wkt(
    geometry: _ArrayLikeAnyStr, on_invalid: str = ..., **kwargs
) -> _NDArrayGeometry: ...
@overload
def from_wkt(geometry: None, on_invalid: str = ..., **kwargs) -> None: ...
@overload
def from_wkb(geometry: AnyStr, on_invalid: str = ..., **kwargs) -> BaseGeometry: ...
@overload
def from_wkb(
    geometry: _ArrayLikeAnyStr, on_invalid: str = ..., **kwargs
) -> _NDArrayGeometry: ...
@overload
def from_wkb(geometry: None, on_invalid: str = ..., **kwargs) -> None: ...
@overload
def from_geojson(geometry: AnyStr, on_invalid: str = ..., **kwargs) -> BaseGeometry: ...
@overload
def from_geojson(
    geometry: _ArrayLikeAnyStr, on_invalid: str = ..., **kwargs
) -> _NDArrayGeometry: ...
@overload
def from_geojson(geometry: None, on_invalid: str = ..., **kwargs) -> None: ...
