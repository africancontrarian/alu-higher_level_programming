#!/usr/bin/python3
"""Defines a function that prints a person's full name.

Provides ``say_my_name``, which validates that both the first and
last names are strings before printing a formatted greeting.
"""


def say_my_name(first_name, last_name=""):
    """Print 'My name is <first name> <last name>'.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print. Defaults to "".

    Raises:
        TypeError: If ``first_name`` is not a string.
        TypeError: If ``last_name`` is not a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
