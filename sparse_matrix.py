from collections import namedtuple
from random import randint

MAX_VALUE = 255
N_SIZE = 9 * 1 * 2

Cell = namedtuple('Cell', ['y', 'x', 'value'])  # for clarity


class SparseMatrix:
    def __init__(self, x_size: int, y_size: int):
        self.x_size = x_size
        self.y_size = y_size
        self.elements = [Cell(randint(0, N_SIZE), randint(0, N_SIZE), randint(-MAX_VALUE, MAX_VALUE))
                         for _ in range(N_SIZE * N_SIZE)]
