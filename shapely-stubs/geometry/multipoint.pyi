from shapely.geometry.base import BaseMultipartGeometry

from .._typing import _ArrayLikeFloat, _ArrayLikeGeometry

class MultiPoint(BaseMultipartGeometry):
    def __new__(
        self, points: _ArrayLikeGeometry | _ArrayLikeFloat | MultiPoint | None = ...
    ): ...
    def svg(  # type: ignore[override]
        self,
        scale_factor: float = ...,
        fill_color: str | None = ...,
        opacity: float | str | None = ...,
    ) -> str: ...
