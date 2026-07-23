#!/usr/bin/python3
"""Defines a function that inserts a line after every matching line
in a file."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text into a file after each line that
    contains a given search string.

    Args:
        filename (str): The path to the text file to modify.
        search_string (str): The substring to search for in each
            line of the file.
        new_string (str): The line of text to insert after every
            line containing search_string.
    """
    with open(filename, encoding="utf-8") as a_file:
        lines = a_file.readlines()

    with open(filename, "w", encoding="utf-8") as a_file:
        for line in lines:
            a_file.write(line)
            if search_string in line:
                a_file.write(new_string)
