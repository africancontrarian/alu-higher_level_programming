#!/usr/bin/python3
"""Defines a function that checks if an object belongs to a
subclass (direct or indirect) of a given class, excluding the
exact class itself."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a subclass (direct or
    indirect) of a_class, but not an instance of a_class itself.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj's type descends (directly or
            indirectly) of a_class without being a_class, False
            otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
