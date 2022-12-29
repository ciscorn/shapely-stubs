from typing import Any

from shapely.geometry.base import BaseMultipartGeometry

class MultiPolygon(BaseMultipartGeometry):
    def __new__(self, polygons: Any = ...): ...
    def svg(  # type: ignore[override]
        self,
        scale_factor: float = ...,
        fill_color: str | None = ...,
        opacity: float | str | None = ...,
    ) -> str: ...
