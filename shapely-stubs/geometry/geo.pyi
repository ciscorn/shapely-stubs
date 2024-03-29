from abc import abstractmethod
from typing import Any, Protocol

from shapely.errors import GeometryTypeError as GeometryTypeError
from shapely.geometry.base import BaseGeometry

from .collection import GeometryCollection as GeometryCollection
from .linestring import LineString as LineString
from .multilinestring import MultiLineString as MultiLineString
from .multipoint import MultiPoint as MultiPoint
from .multipolygon import MultiPolygon as MultiPolygon
from .point import Point as Point
from .polygon import LinearRing as LinearRing
from .polygon import Polygon as Polygon

class GeoInterface(Protocol):
    @property
    @abstractmethod
    def __geo_interface__(self) -> Any: ...

def box(
    minx: float, miny: float, maxx: float, maxy: float, ccw: bool = ...
) -> Polygon: ...
def shape(context: dict | GeoInterface) -> BaseGeometry: ...
def mapping(ob: BaseGeometry) -> dict[str, Any]: ...
