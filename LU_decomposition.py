from copy import deepcopy

from matrix import Matrix


# def lu_decomposition(A: Matrix):
#     n = A.x_size
#     L = Matrix(n, n, 0)
#     U = Matrix(n, n, 0)
#
#     for i in range(n):
#         if A.values[i][i] == 0:
#             raise ValueError("Diagonal element is 0")
#
#         for k in range(i, n):
#             total = 0
#             for j in range(i):
#                 total += (L.values[i][j] * U.values[j][k])
#             U.values[i][k] = A.values[i][k] - total
#
#         for k in range(i, n):
#             if i == k:
#                 L.values[i][i] = 1
#             else:
#                 total = 0
#                 for j in range(i):
#                     total += L.values[k][j] * U.values[j][i]
#                 L.values[k][i] = (A.values[k][i] - total) / U.values[i][i]
#
#     return L, U

def lu_decomposition(A: Matrix):
    n = A.x_size
    L = Matrix(n, n, 0)
    U = deepcopy(A)

    for k in range(n):
        L.values[k][k] = 1

        for i in range(k+1, n):
            if U.values[k][k] == 0:
                raise ValueError("LU decomposition failed: zero pivot encountered")
            factor = U.values[i][k] / U.values[k][k]
            L.values[i][k] = factor
            for j in range(k, n):
                U.values[i][j] = U.values[i][j] - factor * U.values[k][j]

    return L, U


def forward_substitution(A: Matrix, b: Matrix):
    x = Matrix(b.x_size, b.y_size, 0)
    n = A.y_size
    for i in range(n):
        total = 0
        for j in range(i):
            total += A.values[i][j] * x.values[j][0]
        x.values[i][0] = (b.values[i][0] - total) / A.values[i][i]

    return x


def back_substitution(A: Matrix, b: Matrix):
    x = Matrix(b.x_size, b.y_size)
    n = A.y_size

    for i in range(n - 1, -1, -1):
        total = 0
        for j in range(n - 1, i, -1):
            total += A.values[i][j] * x.values[j][0]
        x.values[i][0] = (b.values[i][0] - total) / A.values[i][i]

    return x
