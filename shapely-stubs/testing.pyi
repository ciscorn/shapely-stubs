from shapely.geometry.base import BaseGeometry

from ._typing import _ArrayLikeGeometry

def assert_geometries_equal(
    x: BaseGeometry | _ArrayLikeGeometry | None,
    y: BaseGeometry | _ArrayLikeGeometry | None,
    tolerance: float = ...,
    equal_none: bool = ...,
    equal_nan: bool = ...,
    normalize: bool = ...,
    err_msg: str = ...,
    verbose: bool = ...,
) -> None: ...
