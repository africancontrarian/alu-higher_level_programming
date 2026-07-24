#!/usr/bin/python3
"""Defines a function that adds two integers together.

This module provides a single utility, ``add_integer``, used to
demonstrate basic type validation and casting rules required by the
ALU Test-driven development project.
"""


def add_integer(a, b=98):
    """Add two integers or floats and return the result as an integer.

    Args:
        a (int or float): The first value to add.
        b (int or float): The second value to add. Defaults to 98.

    Returns:
        int: The sum of ``a`` and ``b`` after casting both to int.

    Raises:
        TypeError: If ``a`` is not an int or a float.
        TypeError: If ``b`` is not an int or a float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
