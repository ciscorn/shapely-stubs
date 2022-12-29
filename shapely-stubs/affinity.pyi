from typing_extensions import Literal

from ._typing import _ArrayLikeFloat
from .geometry.base import BaseGeometry

def affine_transform(geom: BaseGeometry, matrix: _ArrayLikeFloat): ...
def rotate(
    geom: BaseGeometry,
    angle: float,
    origin: Literal["center", "centroid"] | _ArrayLikeFloat = ...,
    use_radians: bool = ...,
): ...
def scale(
    geom: BaseGeometry,
    xfact: float = ...,
    yfact: float = ...,
    zfact: float = ...,
    origin: str = ...,
): ...
def skew(
    geom: BaseGeometry,
    xs: float = ...,
    ys: float = ...,
    origin: str = ...,
    use_radians: bool = ...,
): ...
def translate(
    geom: BaseGeometry, xoff: float = ..., yoff: float = ..., zoff: float = ...
): ...
