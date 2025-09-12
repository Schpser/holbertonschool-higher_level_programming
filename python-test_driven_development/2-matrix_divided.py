#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains a function to divide a matrix by a number
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number

    Args:
        matrix: list of lists of integers/floats
        div: number to divide by (cannot be zero)

    Returns:
        list: new matrix with elements divided and rounded

    Raises:
        TypeError: if matrix is not a valid matrix
        TypeError: if rows have different sizes
        TypeError: if div is not a number
        ZeroDivisionError: if div is zero
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


    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            result = element / div
            if abs(result) < 1e-10:
                new_row.append(0.0)
            else:
                new_row.append(round(result, 2))
        new_matrix.append(new_row)

    return new_matrix
