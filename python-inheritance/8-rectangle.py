#!/usr/bin/python3
"""Defines the Rectangle class, a descendant of BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle, extending the BaseGeometry class."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle. Must be a
                positive integer.
            height (int): The height of the rectangle. Must be a
                positive integer.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
