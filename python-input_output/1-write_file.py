#!/usr/bin/python3
"""Defines a function that writes text to a file."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file, creating it if it
    doesn't exist or overwriting it if it does, and return the
    number of characters written.

    Args:
        filename (str): The path to the file to write to.
        text (str): The text to write.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
