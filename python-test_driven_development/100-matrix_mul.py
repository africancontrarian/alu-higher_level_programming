#!/usr/bin/python3
"""Defines a function that multiplies two matrices.

Provides ``matrix_mul``, which validates both operands thoroughly
before computing their matrix product.
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices and return the resulting matrix.

    Args:
        m_a (list): The left-hand matrix (list of lists of int/float).
        m_b (list): The right-hand matrix (list of lists of int/float).

    Returns:
        list: The matrix product of ``m_a`` and ``m_b``.

    Raises:
        TypeError: If ``m_a`` or ``m_b`` is not a list, is not a list
            of lists, contains non-numeric elements, or has rows of
            differing sizes.
        ValueError: If ``m_a`` or ``m_b`` is empty, or if the two
            matrices can't be multiplied together.
    """
    for matrix, name in ((m_a, "m_a"), (m_b, "m_b")):
        if not isinstance(matrix, list):
            raise TypeError("{} must be a list".format(name))
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError("{} must be a list of lists".format(name))
        if all(len(row) == 0 for row in matrix):
            raise ValueError("{} can't be empty".format(name))
        for row in matrix:
            for elem in row:
                if type(elem) not in (int, float):
                    raise TypeError(
                        "{} should contain only integers or floats"
                        .format(name))
        row_len = len(matrix[0])
        for row in matrix:
            if len(row) != row_len:
                raise TypeError(
                    "each row of {} must be of the same size".format(name))

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for row in m_a:
        new_row = []
        for col in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += row[k] * m_b[k][col]
            new_row.append(total)
        result.append(new_row)
    return result
