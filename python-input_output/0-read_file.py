#!/usr/bin/python3
"""Defines a function that reads and prints the content of a text
file."""


def read_file(filename=""):
    """Read a UTF8 text file and print its content to stdout.

    Args:
        filename (str): The path to the text file to read.
    """
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read(), end="")
