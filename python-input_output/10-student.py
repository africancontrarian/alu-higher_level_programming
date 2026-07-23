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

    def to_json(self, attrs=None):
        """Return a dictionary representation of this Student's
        simple (JSON-serializable) attributes.

        Args:
            attrs (list): An optional list of attribute names.
                When provided, only those attributes (among the
                ones this Student actually has) are included.
                Otherwise, every attribute is included.

        Returns:
            dict: The requested attribute names mapped to their
                values.
        """
        if type(attrs) is list:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__
