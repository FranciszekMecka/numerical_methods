from copy import deepcopy
from math import inf, fabs
from matrix import Matrix


def jacobi(A: Matrix, b: Matrix):
    diag_A = A.get_diag()
    inv_diag_A = diag_A.get_inverted()
    x = Matrix(b.x_size, b.y_size, 0)
    x.values = [[1] for _ in range(x.y_size)]  # guessing the x to be equal to 1

    # see https://en.wikipedia.org/wiki/Jacobi_method for reference
    T = (inv_diag_A.multiply(A.subtract(diag_A))).multiply_by_scalar(-1)
    C = inv_diag_A.multiply(b)
    error = inf
    while error > pow(10, -9):
        old_x = deepcopy(x)
        x = T.multiply(x).add(C)
        error = fabs(x.subtract(old_x).get_sum())
    return x
