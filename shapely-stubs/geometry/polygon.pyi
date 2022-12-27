from _typeshed import Incomplete
from shapely.geometry.base import BaseGeometry
from shapely.geometry.linestring import LineString

class LinearRing(LineString):
    def __new__(self, coordinates: Incomplete | None = ...): ...
    @property
    def __geo_interface__(self): ...
    def __reduce__(self): ...
    @property
    def is_ccw(self): ...
    @property
    def is_simple(self): ...

class InteriorRingSequence:
    def __init__(self, parent) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    def __len__(self) -> int: ...
    def __getitem__(self, key): ...

class Polygon(BaseGeometry):
    def __new__(
        self, shell: Incomplete | None = ..., holes: Incomplete | None = ...
    ): ...
    @property
    def exterior(self): ...
    @property
    def interiors(self): ...
    @property
    def coords(self) -> None: ...
    @property
    def __geo_interface__(self): ...
    def svg(
        self,
        scale_factor: float = ...,
        fill_color: Incomplete | None = ...,
        opacity: Incomplete | None = ...,
    ): ...
    @classmethod
    def from_bounds(cls, xmin, ymin, xmax, ymax): ...
