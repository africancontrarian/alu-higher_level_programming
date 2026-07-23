#!/usr/bin/python3
"""Defines a function that converts an object's simple attributes
into a JSON-serializable dictionary."""


def class_to_json(obj):
    """Return the dictionary description of an object's simple
    (JSON-serializable) data structure attributes: list,
    dictionary, string, integer, and boolean.

    Args:
        obj: An instance of a class whose attributes are all
            JSON-serializable.

    Returns:
        dict: A dictionary mapping attribute names to their
            values.
    """
    return obj.__dict__
