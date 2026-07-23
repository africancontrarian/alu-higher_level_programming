#!/usr/bin/python3
"""Defines MagicClass, reconstructed from its disassembled bytecode."""
import math


class MagicClass:
    """Represent a circle defined by its radius."""

    def __init__(self, radius=0):
        """Initialize a new MagicClass.

        Args:
            radius (int/float): The radius of the circle. Defaults to 0.

        Raises:
            TypeError: If radius is neither an int nor a float.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self.__radius
