from copy import deepcopy

from matrix import Matrix
from math import inf, fabs


# see https://shorturl.at/jxzH9 for reference
def gauss(A: Matrix, b: Matrix, tolerance: float = 10e-9, iterations: int = 75000) -> Matrix:
    x: Matrix = Matrix(b.x_size, b.y_size)
    error: float = inf

    while error > tolerance and iterations > 0:
        old_x = deepcopy(x)
        for i in range(A.y_size):
            total: float = 0
            for j in range(A.x_size):
                if j != i:
                    total += A.values[i][j] * x.values[j][0]
                x.values[i][0] = (1/A.values[i][i]) * (b.values[i][0] - total)
            error = fabs(x.subtract(old_x).get_sum())
        iterations -= 1
    return x
