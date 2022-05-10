#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_matrix_in = []
        for j in i:
            new_matrix_in.append(j**2)
        new_matrix.append(new_matrix_in)
    return new_matrix
