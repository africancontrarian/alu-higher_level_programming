#!/usr/bin/python3
"""Defines a function that builds Pascal's triangle."""


def pascal_triangle(n):
    """Build Pascal's triangle up to a given number of rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists of integers representing Pascal's
            triangle of n rows, or an empty list if n is less
            than or equal to 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        previous_row = triangle[-1]
        row = [1]
        for j in range(1, i):
            row.append(previous_row[j - 1] + previous_row[j])
        row.append(1)
        triangle.append(row)
    return triangle
