from typing import Iterable, Literal, overload

from ._typing import (
    _ArrayLikeFloat,
    _ArrayLikeGeometry,
    _NDArrayFloat,
    _NDArrayGeometry,
    _NDArrayInt,
)
from .enum import ParamEnum
from .geometry.base import BaseGeometry

class BinaryPredicate(ParamEnum):
    intersects: int
    within: int
    contains: int
    overlaps: int
    crosses: int
    touches: int
    covers: int
    covered_by: int
    contains_properly: int

class STRtree:
    def __init__(
        self, geoms: Iterable[BaseGeometry], node_capacity: int = ...
    ) -> None: ...
    def __len__(self) -> int: ...
    def __reduce__(self): ...
    @property
    def geometries(self) -> _NDArrayGeometry: ...
    def query(
        self,
        geometry: BaseGeometry | _ArrayLikeGeometry,
        predicate: str | None = ...,
        distance: float | _ArrayLikeFloat | None = ...,
    ) -> _NDArrayInt: ...
    @overload
    def nearest(self, geometry: BaseGeometry) -> int | None: ...
    @overload
    def nearest(self, geometry: _ArrayLikeGeometry) -> _NDArrayInt | None: ...
    @overload
    def query_nearest(
        self,
        geometry: BaseGeometry | _ArrayLikeGeometry,
        max_distance: float | None = ...,
        return_distance: Literal[False] = False,
        exclusive: bool = ...,
        all_matches: bool = ...,
    ) -> _NDArrayInt: ...
    @overload
    def query_nearest(
        self,
        geometry: BaseGeometry | _ArrayLikeGeometry,
        max_distance: float | None,
        return_distance: Literal[True],
        exclusive: bool = ...,
        all_matches: bool = ...,
    ) -> tuple[_NDArrayInt, _NDArrayFloat]: ...
    @overload
    def query_nearest(
        self,
        geometry: BaseGeometry | _ArrayLikeGeometry,
        max_distance: float | None = ...,
        *,
        return_distance: Literal[True],
        exclusive: bool = ...,
        all_matches: bool = ...,
    ) -> tuple[_NDArrayInt, _NDArrayFloat]: ...
