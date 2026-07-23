#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of a
given class, or of any class that descends (directly or
indirectly) of it."""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or of a descendant
    (direct or indirect) of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class, or of a
            subclass of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
