from typing import Iterator

from numpy.typing import DTypeLike

from ._typing import _NDArrayFloat

class CoordinateSequence:
    def __init__(self, coords: _NDArrayFloat) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[tuple[float, ...]]: ...
    def __getitem__(self, key: int | slice): ...
    def __array__(self, dtype: DTypeLike = ...): ...
    @property
    def xy(self) -> tuple[_NDArrayFloat, _NDArrayFloat]: ...
