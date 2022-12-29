from shapely._typing import _ArrayLikeGeometry
from shapely.geometry.base import BaseGeometry as BaseGeometry
from shapely.geometry.base import BaseMultipartGeometry as BaseMultipartGeometry

class GeometryCollection(BaseMultipartGeometry):
    def __new__(self, geoms: BaseGeometry | _ArrayLikeGeometry | None = ...): ...
