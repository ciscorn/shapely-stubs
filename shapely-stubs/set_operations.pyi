from typing import overload

from ._typing import _ArrayLikeGeometry
from .geometry.base import BaseGeometry

@overload
def difference(
    a: BaseGeometry, b: BaseGeometry, grid_size: float | None = ..., **kwargs
) -> BaseGeometry: ...
@overload
def difference(
    a: _ArrayLikeGeometry,
    b: BaseGeometry | _ArrayLikeGeometry,
    grid_size: float | None = ...,
    **kwargs
) -> _ArrayLikeGeometry: ...
@overload
def difference(
    a: BaseGeometry | _ArrayLikeGeometry,
    b: _ArrayLikeGeometry,
    grid_size: float | None = ...,
    **kwargs
) -> _ArrayLikeGeometry: ...
@overload
def difference(
    a: None, b: BaseGeometry | None, grid_size: float | None = ..., **kwargs
) -> None: ...
@overload
def difference(
    a: BaseGeometry | None, b: None, grid_size: float | None = ..., **kwargs
) -> None: ...
@overload
def intersection(
    a: BaseGeometry, b: BaseGeometry, grid_size: float | None = ..., **kwargs
) -> BaseGeometry: ...
@overload
def intersection(
    a: _ArrayLikeGeometry,
    b: BaseGeometry | _ArrayLikeGeometry,
    grid_size: float | None = ...,
    **kwargs
) -> _ArrayLikeGeometry: ...
@overload
def intersection(
    a: BaseGeometry | _ArrayLikeGeometry,
    b: _ArrayLikeGeometry,
    grid_size: float | None = ...,
    **kwargs
) -> _ArrayLikeGeometry: ...
@overload
def intersection(
    a: None, b: BaseGeometry | None, grid_size: float | None = ..., **kwargs
) -> None: ...
@overload
def intersection(
    a: BaseGeometry | None, b: None, grid_size: float | None = ..., **kwargs
) -> None: ...
def intersection_all(
    geometries: BaseGeometry | _ArrayLikeGeometry | None,
    axis: int | None = ...,
    **kwargs
) -> BaseGeometry: ...
@overload
def symmetric_difference(
    a: BaseGeometry, b: BaseGeometry, grid_size: float | None = ..., **kwargs
) -> BaseGeometry: ...
@overload
def symmetric_difference(
    a: _ArrayLikeGeometry,
    b: BaseGeometry | _ArrayLikeGeometry,
    grid_size: float | None = ...,
    **kwargs
) -> _ArrayLikeGeometry: ...
@overload
def symmetric_difference(
    a: BaseGeometry | _ArrayLikeGeometry,
    b: _ArrayLikeGeometry,
    grid_size: float | None = ...,
    **kwargs
) -> _ArrayLikeGeometry: ...
@overload
def symmetric_difference(
    a: None, b: BaseGeometry | None, grid_size: float | None = ..., **kwargs
) -> None: ...
@overload
def symmetric_difference(
    a: BaseGeometry | None, b: None, grid_size: float | None = ..., **kwargs
) -> None: ...
def symmetric_difference_all(
    geometries: BaseGeometry | _ArrayLikeGeometry | None,
    axis: int | None = ...,
    **kwargs
) -> BaseGeometry: ...
@overload
def union(
    a: BaseGeometry, b: BaseGeometry, grid_size: float | None = ..., **kwargs
) -> BaseGeometry: ...
@overload
def union(
    a: _ArrayLikeGeometry,
    b: BaseGeometry | _ArrayLikeGeometry,
    grid_size: float | None = ...,
    **kwargs
) -> _ArrayLikeGeometry: ...
@overload
def union(
    a: BaseGeometry | _ArrayLikeGeometry,
    b: _ArrayLikeGeometry,
    grid_size: float | None = ...,
    **kwargs
) -> _ArrayLikeGeometry: ...
@overload
def union(
    a: None, b: BaseGeometry | None, grid_size: float | None = ..., **kwargs
) -> None: ...
@overload
def union(
    a: BaseGeometry | None, b: None, grid_size: float | None = ..., **kwargs
) -> None: ...
def union_all(
    geometries: BaseGeometry | _ArrayLikeGeometry | None,
    grid_size: float | None = ...,
    axis: int | None = ...,
    **kwargs
) -> BaseGeometry: ...

unary_union = union_all

@overload
def coverage_union(
    a: BaseGeometry | None, b: BaseGeometry | None, **kwargs
) -> BaseGeometry: ...
@overload
def coverage_union(
    a: _ArrayLikeGeometry, b: _ArrayLikeGeometry, **kwargs
) -> _ArrayLikeGeometry: ...
def coverage_union_all(
    geometries: BaseGeometry | _ArrayLikeGeometry | None,
    axis: int | None = ...,
    **kwargs
) -> BaseGeometry: ...
