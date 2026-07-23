#!/usr/bin/python3
"""Defines a function that looks up the attributes and methods of
an object."""


def lookup(obj):
    """Return the list of available attributes and methods of obj.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list containing the names of all attributes and
            methods available on obj.
    """
    return dir(obj)
