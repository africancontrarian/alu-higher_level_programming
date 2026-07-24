#!/usr/bin/python3
"""Defines the Base class, the foundation of all other classes here.

The ``Base`` class manages the ``id`` attribute for every object of the
project and provides the JSON and CSV serialization/deserialization
helpers shared by ``Rectangle`` and ``Square``.
"""
import json
import csv


class Base:
    """Represents the base of all the classes in this project.

    It keeps track of the number of instances created so it can hand
    out a unique ``id`` automatically when none is supplied.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The identity of the new instance. When ``None``,
                the number of created objects is incremented and used.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: ``"[]"`` if the list is ``None`` or empty, otherwise
            the JSON string representation of the list.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of a list of objects to a file.

        The file is named ``<Class name>.json`` and is overwritten if
        it already exists.

        Args:
            list_objs (list): A list of instances that inherit from
                Base. ``None`` is treated as an empty list.
        """
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as jsonfile:
            jsonfile.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string.

        Args:
            json_string (str): A JSON string representing a list of
                dictionaries.

        Returns:
            list: An empty list if ``json_string`` is ``None`` or
            empty, otherwise the Python list it represents.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.

        A "dummy" instance is created first and then updated with the
        real values held in ``dictionary``.

        Args:
            **dictionary: Key/value pairs of attributes to set.

        Returns:
            Base: A new instance of ``cls`` with the given attributes.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from ``<Class name>.json``.

        Returns:
            list: An empty list if the file does not exist, otherwise a
            list of instances of ``cls``.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = cls.from_json_string(jsonfile.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV representation of a list of objects to a file.

        The file is named ``<Class name>.csv`` and is overwritten if it
        already exists.

        Args:
            list_objs (list): A list of instances that inherit from
                Base. ``None`` is treated as an empty list.
        """
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        if list_objs is None:
            list_objs = []
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances loaded from ``<Class name>.csv``.

        Returns:
            list: An empty list if the file does not exist, otherwise a
            list of instances of ``cls``.
        """
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        try:
            with open(filename, "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile, fieldnames=fields)
                list_dicts = [
                    {key: int(value) for key, value in row.items()}
                    for row in reader
                ]
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in list_dicts]
