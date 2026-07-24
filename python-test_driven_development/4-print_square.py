#!/usr/bin/python3
"""Defines a function that prints a square made of the '#' character.

Provides ``print_square``, which validates that the given size is a
non-negative integer before drawing the square.
"""


def print_square(size):
    """Print a square of '#' characters, one row per print call.

    Args:
        size (int): The length of each side of the square.

    Raises:
        TypeError: If ``size`` is not an integer.
        ValueError: If ``size`` is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
