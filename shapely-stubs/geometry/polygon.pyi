from typing import Sequence

from shapely.geometry.base import BaseGeometry
from shapely.geometry.linestring import LineString
from typing_extensions import NoReturn

from .._typing import _ArrayLikeFloat, _NDArrayFloat

class LinearRing(LineString):
    def __new__(self, coordinates: LineString | _NDArrayFloat | None = ...): ...
    def __reduce__(self): ...
    @property
    def is_ccw(self) -> bool: ...
    @property
    def is_simple(self) -> bool: ...

class InteriorRingSequence:
    def __init__(self, parent) -> None: ...
    def __iter__(self) -> InteriorRingSequence: ...
    def __next__(self) -> LinearRing: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key): ...

class Polygon(BaseGeometry):
    def __new__(
        self,
        shell: BaseGeometry | _ArrayLikeFloat | Polygon | None = ...,
        holes: Sequence[LineString] | _ArrayLikeFloat | None = ...,
    ): ...
    @property
    def exterior(self) -> LinearRing: ...
    @property
    def interiors(self) -> InteriorRingSequence | list: ...
    @property
    def coords(self) -> NoReturn: ...
    def svg(  # type: ignore[override]
        self,
        scale_factor: float = ...,
        fill_color: str | None = ...,
        opacity: float | None = ...,
    ) -> str: ...
    @classmethod
    def from_bounds(
        cls, xmin: float, ymin: float, xmax: float, ymax: float
    ) -> Polygon: ...
