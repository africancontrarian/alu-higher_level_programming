#!/usr/bin/python3
"""Defines the Rectangle class, a Base subclass with size and position.

A ``Rectangle`` validates its width, height and coordinates, can draw
itself, and can be serialized to and from a dictionary.
"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle that inherits its id from ``Base``.

    Width, height and the ``x``/``y`` position are stored in private
    attributes protected by validating getters and setters.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The horizontal offset of the rectangle.
            y (int): The vertical offset of the rectangle.
            id (int): The identity of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width after validating it is a positive integer."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height after validating it is a positive integer."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: The horizontal offset of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x after validating it is a non-negative integer."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: The vertical offset of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y after validating it is a non-negative integer."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle with the ``#`` character.

        The ``y`` offset produces blank lines above the shape and the
        ``x`` offset produces spaces to the left of each row.
        """
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return the string description of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update the rectangle's attributes.

        Args:
            *args: New attribute values in the order id, width, height,
                x, y. When present, ``kwargs`` is ignored.
            **kwargs: New attribute values given by name.
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
