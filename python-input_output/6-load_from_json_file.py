#!/usr/bin/python3
"""Defines a function that loads a Python object from a JSON
file."""
import json


def load_from_json_file(filename):
    """Create a Python data structure from the JSON content of a
    file.

    Args:
        filename (str): The path to the JSON file to read.

    Returns:
        The Python data structure described by the file's content.
    """
    with open(filename, encoding="utf-8") as a_file:
        return json.load(a_file)
