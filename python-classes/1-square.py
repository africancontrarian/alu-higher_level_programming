#!/usr/bin/python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Represent a square with a private, unvalidated size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
