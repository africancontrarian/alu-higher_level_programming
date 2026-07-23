#!/usr/bin/python3
"""Defines a function that saves a Python object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Write the JSON representation of an object to a text file.

    Args:
        my_obj: The Python data structure to serialize.
        filename (str): The path to the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
