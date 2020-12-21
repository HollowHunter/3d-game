from numba import njit, jit
import numba as nb
# from numba import types
import numpy as np
from pygame import time

# from math import cos, radians

clock = time.Clock()



@jit((nb.float_[::1], nb.float_[::1]))
def m_sum(matrix_a, matrix_b):
    if isinstance(matrix_a, (int, float)) and isinstance(matrix_b, (int, float)):
        return matrix_a + matrix_b
    elif isinstance(matrix_a, (int, float)) and not isinstance(matrix_b, (int, float)):
        print('error: mat_a size != mat_b size\n', matrix_a, '\n', matrix_b)
    elif not isinstance(matrix_a, (int, float)) and isinstance(matrix_b, (int, float)):
        print('error: mat_a size != mat_b size\n', matrix_a, '\n', matrix_b)

    res = []
    for a, b in zip(matrix_a, matrix_b):
        res.append(m_sum(a, b))

    return tuple(res) if isinstance(res, tuple) else res

print(m_sum([1, 2, [3]], [1, 2, [3]]))
print(m_sum([1, 2, (1, 3)], [1, 2, (3, 1)]))