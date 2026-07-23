#!/usr/bin/python3
"""Defines a function that checks if an object is exactly an
instance of a given class."""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the exact type of obj is a_class, otherwise
            False.
    """
    return type(obj) == a_class
