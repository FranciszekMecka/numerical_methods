from matrix import Matrix
from math import sin

C = 1
D = 2
E = 7
F = 1
N_SIZE = 9 * C * D


def get_data(a1: float = E + 5, a2: float = -1, a3: float = -1, size: int = N_SIZE) -> Matrix:
    mat_data = Matrix(size, size, 0)
    vect_data = Matrix(1, size, 0)
    for i in range(size):
        vect_data.values[i][0] = sin(i * (F + 1))
        for j in range(size):
            if i != 0 and j != 0:
                mat_data.values[i][i - 1] = a2
                if i != 1 and j != 1:
                    mat_data.values[i][i - 2] = a3
            if i != size - 1 and j != 0:
                mat_data.values[i][i + 1] = a2
                if i != size - 2 and j != 1:
                    mat_data.values[i][i + 2] = a3
            mat_data.values[i][i] = a1

    return mat_data, vect_data
