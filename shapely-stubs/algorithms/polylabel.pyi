from shapely.geometry.polygon import Polygon

from ..errors import TopologicalError as TopologicalError
from ..geometry import Point as Point

class Cell:
    x: float
    y: float
    h: float
    centroid: Point
    distance: float
    max_distance: float
    def __init__(self, x, y, h, polygon) -> None: ...
    def __lt__(self, other: Cell) -> bool: ...
    def __le__(self, other: Cell) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __gt__(self, other: Cell) -> bool: ...
    def __ge__(self, other: Cell) -> bool: ...

def polylabel(polygon: Polygon, tolerance: float = ...) -> Point: ...
