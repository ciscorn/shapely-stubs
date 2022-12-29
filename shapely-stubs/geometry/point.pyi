from typing import overload

import numpy
from shapely._typing import _ArrayLikeFloat, _NDArrayFloat
from shapely.geometry.base import BaseGeometry

class Point(BaseGeometry):
    @overload
    def __new__(self, _p: Point | _ArrayLikeFloat | None = ...) -> Point: ...
    @overload
    def __new__(
        self,
        _x: float | _ArrayLikeFloat,
        _y: float | _ArrayLikeFloat,
        _z: float | _ArrayLikeFloat | None = ...,
    ) -> Point: ...
    @property
    def x(self) -> numpy.float64: ...
    @property
    def y(self) -> numpy.float64: ...
    @property
    def z(self) -> numpy.float64: ...
    def svg(  # type: ignore[override]
        self,
        scale_factor: float = ...,
        fill_color: str | None = ...,
        opacity: float | str | None = ...,
    ) -> str: ...
    @property
    def xy(self) -> tuple[_NDArrayFloat, _NDArrayFloat]: ...
