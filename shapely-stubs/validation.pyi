from typing import overload

from shapely.geometry.base import BaseGeometry

from ._typing import _ArrayLikeGeometry, _NDArrayObject

@overload
def explain_validity(ob: BaseGeometry) -> str: ...
@overload
def explain_validity(ob: _ArrayLikeGeometry) -> _NDArrayObject: ...
@overload
def explain_validity(ob: None) -> None: ...
def make_valid(ob: BaseGeometry) -> BaseGeometry: ...
