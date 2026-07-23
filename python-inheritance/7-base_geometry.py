#!/usr/bin/python3
"""Defines the BaseGeometry class with a placeholder area method
and a helper that validates positive integer attributes."""


class BaseGeometry:
    """Represents a base for every geometry shape in this project."""

    def area(self):
        """Raise an exception, since computing an area is left to
        each specific shape that descends of this base class."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a given value is a positive integer.

        Args:
            name (str): The name of the attribute being validated,
                used to build a readable error message.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
