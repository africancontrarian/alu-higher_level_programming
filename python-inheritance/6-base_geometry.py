#!/usr/bin/python3
"""Defines the BaseGeometry class with a placeholder area method."""


class BaseGeometry:
    """Represents a base for every geometry shape in this project."""

    def area(self):
        """Raise an exception, since computing an area is left to
        each specific shape that descends of this base class."""
        raise Exception("area() is not implemented")
