from copy import deepcopy
from random import randint
from math import sin

E = 7


class Matrix:
    # creates matrix of size X*Y with given value
    def __init__(self, x_size: int, y_size: int, value: float = 0):
        self.x_size: int = x_size
        self.y_size: int = y_size
        self.values: list = [[value for _ in range(x_size)] for _ in range(y_size)]

    # populates the matrix with set data
    def populate_matrix(self):
        a1: float = 5 + E
        a2: float = -1
        a3: float = -1
        for i in range(len(self.values)):
            self.values[i][i] = a1
            if i != 0:
                self.values[i - 1][i] = a2
                if i != 1:
                    self.values[i - 2][i] = a3
            if i != len(self.values) - 1:
                self.values[i + 1][i] = a2
                if i != len(self.values) - 2:
                    self.values[i + 2][i] = a3

    def populate_matrix_random(self):
        for i in range(self.y_size):
            for j in range(self.x_size):
                self.values[i][j] = randint(1, 9)

    def populate_vector(self):
        f = 1  # third digit of my index
        for n in range(self.y_size):
            self.values[n][self.x_size - 1] = sin(n * (f + 1))  # vector has height == 1

    def get_diag(self):
        diag = Matrix(self.x_size, self.y_size, 0)
        for i in range(self.x_size):
            diag.values[i][i] = self.values[i][i]
        return diag

    def get_inverted(self):
        result = deepcopy(self)
        for y in range(result.y_size):
            for x in range(result.x_size):
                if result.values[y][x] != 0:
                    result.values[y][x] = pow(result.values[y][x], -1)
        return result

    def subtract(self, mat):
        result = deepcopy(self)
        for y in range(result.y_size):
            for x in range(result.x_size):
                result.values[y][x] -= mat.values[y][x]
        return result

    def add(self, mat):
        result = deepcopy(self)

        if self.x_size != mat.x_size and self.y_size != mat.y_size:
            raise ValueError("Matrices are not compatible for addition")

        for y in range(result.y_size):
            for x in range(result.x_size):
                result.values[y][x] += mat.values[y][x]
        return result

    def multiply(self, mat):
        result = Matrix(mat.x_size, self.y_size, 0)

        if self.x_size != mat.y_size:
            raise ValueError("Matrices are not compatible for multiplication")

        for i in range(result.y_size):
            for j in range(result.x_size):
                dot_product = 0
                for k in range(self.x_size):
                    dot_product += self.values[i][k] * mat.values[k][j]
                result.values[i][j] = dot_product

        return result

    def get_sum(self) -> float:
        value_sum = 0
        for i in range(self.y_size):
            for j in range(self.x_size):
                value_sum += self.values[i][j]
        return value_sum

    def multiply_by_scalar(self, scalar: float):
        result = deepcopy(self)
        for i in range(result.y_size):
            for j in range(result.x_size):
                result.values[i][j] *= scalar
                if result.values[i][j] == 0.0:  # there is minus zero, I don't know if this will cause any
                    # issues later
                    result.values[i][j] = 0

        return result

    def get_triangle(self, mat_type: str = 'L'):
        tri = Matrix(self.x_size, self.y_size, 0)

        if mat_type == 'L':
            y = 1
            k = 0
            for x in range(self.x_size):
                y += k
                while y < self.y_size:
                    tri.values[y][x] = self.values[y][x]
                    y += 1
                y = 1
                k += 1

        elif mat_type == 'U':
            y = self.y_size - 1 - 1  # to avoid diag
            k = 0
            for x in range(self.x_size - 1, 0, -1):
                y -= k
                while y >= 0:
                    tri.values[y][x] = self.values[y][x]
                    y -= 1
                y = self.y_size - 1 - 1  # to avoid diag
                k += 1

        return tri

    def print(self):
        for row in self.values:
            print(row)
