#!/usr/bin/python3
"""Defines a function that appends text to a file."""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF8 text file, creating
    the file first if it doesn't exist, and return the number of
    characters added.

    Args:
        filename (str): The path to the file to append to.
        text (str): The text to append.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
