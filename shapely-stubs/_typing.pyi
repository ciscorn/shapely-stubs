from typing import Any, AnyStr, TypeVar, Union

import numpy
from numpy._typing import NDArray, _NestedSequence, _SupportsArray

from .geometry.base import BaseGeometry

_T = TypeVar("_T")
_DType = TypeVar("_DType", bound=numpy.dtype[Any])

_NDArrayGeometry = NDArray[numpy.object_]
_NDArrayFloat = NDArray[numpy.floating]
_NDArrayInt = NDArray[numpy.integer]
_NDArrayObject = NDArray[numpy.object_]
_NDArrayBool = NDArray[numpy.bool_]

# array_like except for scalar
_ArrayLike = Union[
    _SupportsArray[_DType],
    _NestedSequence[_SupportsArray[_DType]],
    _NestedSequence[_T],
]

_ArrayLikeFloat = _ArrayLike[
    numpy.dtype[Union[numpy.bool_, numpy.integer[Any], numpy.floating[Any]]],
    Union[bool, int, float],
]
_ArrayLikeInt = _ArrayLike[numpy.dtype[numpy.integer[Any]], int]
_ArrayLikeBool = _ArrayLike[numpy.dtype[numpy.bool_], bool]
_ArrayLikeAnyStr = _ArrayLike[
    numpy.dtype[Union[numpy.str_, numpy.bytes_, numpy.object_]], AnyStr
]
_ArrayLikeObject = _ArrayLike[numpy.dtype[numpy.object_], object]
_ArrayLikeGeometry = _ArrayLike[numpy.dtype[numpy.object_], BaseGeometry]
