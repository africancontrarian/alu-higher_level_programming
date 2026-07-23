#!/usr/bin/python3
"""Defines a class that extends the built-in list with a sorted
printing capability."""


class MyList(list):
    """Represents a list of integers that can display itself
    sorted without changing its own internal order."""

    def print_sorted(self):
        """Print all the integers of the list in ascending order,
        leaving the original order of the list unchanged."""
        print(sorted(self))
