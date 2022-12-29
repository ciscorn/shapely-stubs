from typing import Literal

from shapely.geometry.base import BaseGeometry

from .._typing import _ArrayLikeFloat, _ArrayLikeGeometry
from ..geometry import MultiLineString
from ..geometry.base import JOIN_STYLE

class LineString(BaseGeometry):
    def __new__(
        self,
        coordinates: _ArrayLikeFloat | _ArrayLikeGeometry | LineString | None = ...,
    ): ...
    def svg(  # type: ignore[override]
        self,
        scale_factor: float = ...,
        stroke_color: str | None = ...,
        opacity: float | str | None = ...,
    ) -> str: ...
    def offset_curve(
        self,
        distance: float,
        quad_segs: int = ...,
        join_style: JOIN_STYLE = ...,
        mitre_limit: float = ...,
    ) -> LineString | MultiLineString: ...
    def parallel_offset(
        self,
        distance: float,
        side: Literal["right", "left"] = ...,
        resolution: int = ...,
        join_style: JOIN_STYLE = ...,
        mitre_limit: float = ...,
    ): ...
