from shapely.geometry.base import BaseMultipartGeometry

from .._typing import _ArrayLikeFloat, _ArrayLikeGeometry

class MultiLineString(BaseMultipartGeometry):
    def __new__(
        self, lines: _ArrayLikeFloat | _ArrayLikeGeometry | MultiLineString | None = ...
    ): ...
    def svg(  # type: ignore[override]
        self,
        scale_factor: float = ...,
        stroke_color: str | None = ...,
        opacity: float | str | None = ...,
    ) -> str: ...
