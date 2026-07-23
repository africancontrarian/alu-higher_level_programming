#!/usr/bin/python3
"""Defines a rebellious integer class."""


class MyInt(int):
    """Represents an integer whose equality operators are inverted:
    what would normally be equal is reported as different, and what
    would normally be different is reported as equal."""

    def __eq__(self, value):
        """Return the opposite of the normal equality comparison."""
        return int(self) != value

    def __ne__(self, value):
        """Return the opposite of the normal inequality comparison."""
        return int(self) == value

    __hash__ = int.__hash__
