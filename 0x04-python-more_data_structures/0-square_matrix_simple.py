#!/usr/bin/python3

def square_matrix_simple(matrix=None):
    if not matrix:
        return matrix

    n = len(matrix)
    m = len(matrix[0])

    new_matrix = [row[:] for row in matrix]

    for i in range(n):
        for j in range(m):
            new_matrix[i][j] *= new_matrix[i][j]

    return new_matrix
