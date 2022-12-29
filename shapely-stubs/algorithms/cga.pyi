from typing import Callable, Union

import numpy
import numpy as np

from ..geometry.base import BaseGeometry
from ..geometry.polygon import LinearRing

def signed_area(ring: LinearRing) -> numpy.float64: ...
def is_ccw_impl(name=None) -> Callable[[BaseGeometry], Union[np.bool_, bool]]: ...
