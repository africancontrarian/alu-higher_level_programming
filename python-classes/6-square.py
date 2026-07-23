#!/usr/bin/python3
"""Defines a Square class with size and position properties."""


class Square:
    """Represent a square with a validated size and a 2D print position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square. Defaults to 0.
            position (tuple): The (x, y) position used when printing the
                square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current (x, y) print position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the print position of the square.

        Args:
            value (tuple): A tuple of 2 non-negative integers, (x, y).

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (type(value) is not tuple or
                len(value) != 2 or
                not all(type(coord) is int for coord in value) or
                not all(coord >= 0 for coord in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square to stdout using the `#` character.

        The square is offset by `position`: position[0] adds that many
        leading spaces to every printed row, and position[1] adds that
        many blank lines above the square. Lines are never padded with
        trailing spaces. Prints a single empty line if size is 0.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
