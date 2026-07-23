#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represents a student with a first name, last name, and
    age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of this Student's
        simple (JSON-serializable) attributes."""
        return self.__dict__
