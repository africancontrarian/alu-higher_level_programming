#!/usr/bin/python3
"""Defines a function that safely adds a new attribute to an
object, when that kind of object supports it."""


def add_attribute(obj, name, value):
    """Add a new attribute to obj, if obj supports it.

    Args:
        obj: The object to modify.
        name (str): The name of the new attribute.
        value: The value to assign to the new attribute.

    Raises:
        TypeError: If obj cannot receive new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
