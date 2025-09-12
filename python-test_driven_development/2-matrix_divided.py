#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains a function to divide a matrix by a number
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                msg = "matrix must be a matrix (list of lists) of integers/floats"
                raise TypeError(msg)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if abs(div) == float('inf'):
        return [[0.0 for _ in row] for row in matrix]

    return [[round(element / div, 2) for element in row] for row in matrix]
