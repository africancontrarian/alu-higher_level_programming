#!/usr/bin/python3
"""Defines the Square class, a special Rectangle with equal sides.

A ``Square`` reuses every attribute, validation rule and method of
``Rectangle`` while exposing a single ``size`` property.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, a rectangle whose width equals its height."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The length of each side of the square.
            x (int): The horizontal offset of the square.
            y (int): The vertical offset of the square.
            id (int): The identity of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: The length of the square's sides (its width)."""
        return self.width

    @size.setter
    def size(self, value):
        """Set both the width and the height to ``value``."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string description of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the square's attributes.

        Args:
            *args: New attribute values in the order id, size, x, y.
                When present, ``kwargs`` is ignored.
            **kwargs: New attribute values given by name.
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
