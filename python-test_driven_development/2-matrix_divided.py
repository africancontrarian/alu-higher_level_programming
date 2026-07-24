#!/usr/bin/python3
"""Defines a function that divides all the elements of a matrix.

The module exposes ``matrix_divided``, which validates its inputs
strictly before performing an element-wise division and rounding
every result to two decimal places.
"""


def matrix_divided(matrix, div):
    """Divide every element of a matrix by a given divisor.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int or float): The number every element is divided by.

    Returns:
        list: A new matrix with every element divided by ``div`` and
        rounded to 2 decimal places.

    Raises:
        TypeError: If ``matrix`` is not a list of lists of
            integers/floats, or if its rows are not all the same size.
        TypeError: If ``div`` is not an integer or a float.
        ZeroDivisionError: If ``div`` is equal to 0.
    """
    matrix_err = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(matrix_err)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(matrix_err)
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError(matrix_err)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
