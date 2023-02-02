"""Functions that use the API to perform basic math operations.

These functions are meant for proof-of-concept and testing.
For example usage, refer to the demos directory of this repository.
"""
import numpy as np
from .api import invoke_api
# pylint: disable=unused-argument, disable=redefined-builtin


def sum(a: float, b: float) -> float:
    return invoke_api(locals(), sum)


def matmul(m: np.ndarray, n: np.ndarray) -> np.ndarray:
    return invoke_api(locals(), matmul)


# pylint: enable=unused-argument, enable=redefined-builtin
