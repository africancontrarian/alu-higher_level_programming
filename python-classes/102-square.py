#!/usr/bin/python3
"""Defines a Square class comparable by area."""


class Square:
    """Represent a square whose instances compare by area."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int/float): The size of the new square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int/float): The new size of the square.

        Raises:
            TypeError: If value is not a number (int or float).
            ValueError: If value is less than 0.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Check whether this square's area equals other's area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check whether this square's area differs from other's area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check whether this square's area is less than other's area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check whether this square's area is at most other's area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check whether this square's area is greater than other's area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check whether this square's area is at least other's area."""
        return self.area() >= other.area()
