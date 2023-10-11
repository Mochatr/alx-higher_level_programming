#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = matrix.copy()

    for n in range(len(matrix)):
        newMatrix[n] = list(map(lambda x: x**2, matrix[n]))

    return newMatrix
