#!/usr/bin/python3
"""Defines a function that prints text with extra line breaks.

Provides ``text_indentation``, which prints a block of text while
inserting two newlines after every '.', '?', and ':' character.
"""


def text_indentation(text):
    """Print a text, adding 2 new lines after '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If ``text`` is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        if char == " " and line == "":
            continue
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
