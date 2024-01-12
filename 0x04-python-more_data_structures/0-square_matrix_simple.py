#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    newRow = []
    for row in matrix:
        for x in row:
            newRow.append(x**2)
        newMatrix.append(newRow)
    return newMatrix
