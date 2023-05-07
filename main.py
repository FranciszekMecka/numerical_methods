from matrix import Matrix
from jacobi import jacobi
from gauss_seidel import gauss
from LU_decomposition import lu_decomposition, forward_substitution, back_substitution
from data import get_data
import time

N_SIZE = 4

if __name__ == '__main__':
    mat, vect = get_data()
    print('Jacobi')
    jacobi(mat, vect).print()
    print('gauss')
    gauss(mat, vect).print()

    print('lu_decomposition')
    L, U = lu_decomposition(mat)
    y = forward_substitution(L, vect)
    x = back_substitution(U, y)
    x.print()

    # data from C task
    # mat, vect = get_data(3, -1, -1)
