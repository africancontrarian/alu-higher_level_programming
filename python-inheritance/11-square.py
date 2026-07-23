#!/usr/bin/python3
"""Defines the Square class, a descendant of Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, extending the Rectangle class."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The length of each side of the square.
                Must be a positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the human-readable description of the square,
        formatted as [Square] <width>/<height>."""
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height)
