#!/usr/bin/python3
"""Unittests for the Square class."""
import unittest
import io
import os
from contextlib import redirect_stdout
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareInstantiation(unittest.TestCase):
    """Tests for creating Square instances."""

    def test_is_rectangle_subclass(self):
        """Square inherits from Rectangle."""
        self.assertIsInstance(Square(1), Rectangle)

    def test_is_base_subclass(self):
        """Square is ultimately a Base."""
        self.assertIsInstance(Square(1), Base)

    def test_size_sets_width_and_height(self):
        """The size argument fills both width and height."""
        s = Square(5)
        self.assertEqual((s.width, s.height), (5, 5))

    def test_position_args(self):
        """x, y and id are forwarded to the Rectangle constructor."""
        s = Square(3, 1, 3, 7)
        self.assertEqual((s.size, s.x, s.y, s.id), (3, 1, 3, 7))

    def test_default_position(self):
        """x and y default to 0."""
        s = Square(4)
        self.assertEqual((s.x, s.y), (0, 0))

    def test_missing_size_raises(self):
        """size is a required argument."""
        with self.assertRaises(TypeError):
            Square()


class TestSquareValidation(unittest.TestCase):
    """Tests that Square reuses Rectangle's validation."""

    def test_non_int_size(self):
        """A non-integer size raises the width TypeError."""
        with self.assertRaises(TypeError) as e:
            Square("4")
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_zero_size(self):
        """A zero size raises the width ValueError."""
        with self.assertRaises(ValueError) as e:
            Square(0)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_negative_size(self):
        """A negative size raises the width ValueError."""
        with self.assertRaises(ValueError):
            Square(-5)

    def test_non_int_x(self):
        """A non-integer x raises the x TypeError."""
        with self.assertRaises(TypeError) as e:
            Square(1, "2")
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_negative_x(self):
        """A negative x raises the x ValueError."""
        with self.assertRaises(ValueError) as e:
            Square(1, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_non_int_y(self):
        """A non-integer y raises the y TypeError."""
        with self.assertRaises(TypeError) as e:
            Square(1, 2, "3")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_negative_y(self):
        """A negative y raises the y ValueError."""
        with self.assertRaises(ValueError) as e:
            Square(1, 2, -3)
        self.assertEqual(str(e.exception), "y must be >= 0")


class TestSquareArea(unittest.TestCase):
    """Tests for the inherited area method."""

    def test_area(self):
        """Area is size squared."""
        self.assertEqual(Square(5).area(), 25)

    def test_area_after_resize(self):
        """Area reflects a resized square."""
        s = Square(2)
        s.size = 4
        self.assertEqual(s.area(), 16)


class TestSquareSize(unittest.TestCase):
    """Tests for the size getter and setter."""

    def test_size_getter(self):
        """The getter returns the current width."""
        self.assertEqual(Square(7).size, 7)

    def test_size_setter(self):
        """The setter updates both width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))

    def test_size_setter_validates(self):
        """The setter reuses the width validation message."""
        s = Square(5)
        with self.assertRaises(TypeError) as e:
            s.size = "9"
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_size_setter_negative(self):
        """A negative size raises the width ValueError."""
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = -1


class TestSquareStr(unittest.TestCase):
    """Tests for the __str__ method."""

    def test_str(self):
        """__str__ follows the documented Square format."""
        s = Square(3, 1, 3, 3)
        self.assertEqual(str(s), "[Square] (3) 1/3 - 3")

    def test_str_default_position(self):
        """__str__ uses the default x and y."""
        s = Square(5, id=1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")


class TestSquareDisplay(unittest.TestCase):
    """Tests for the inherited display method."""

    def test_display(self):
        """A size-2 square prints two rows of two hashes."""
        buf = io.StringIO()
        with redirect_stdout(buf):
            Square(2).display()
        self.assertEqual(buf.getvalue(), "##\n##\n")

    def test_display_with_xy(self):
        """x and y offset the drawing."""
        buf = io.StringIO()
        with redirect_stdout(buf):
            Square(2, 1, 1).display()
        self.assertEqual(buf.getvalue(), "\n ##\n ##\n")


class TestSquareUpdate(unittest.TestCase):
    """Tests for the update method."""

    def test_update_args(self):
        """Positional arguments map to id, size, x, y."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_id_only(self):
        """A single argument updates just the id."""
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)

    def test_update_kwargs(self):
        """Keyword arguments update attributes by name."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")

    def test_args_priority_over_kwargs(self):
        """kwargs are ignored when args are present."""
        s = Square(5)
        s.update(1, 2, size=99)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)


class TestSquareToDictionary(unittest.TestCase):
    """Tests for the to_dictionary method."""

    def test_dictionary_content(self):
        """The dictionary holds id, size, x and y."""
        s = Square(10, 2, 1, 1)
        self.assertEqual(
            s.to_dictionary(), {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_dictionary_type(self):
        """to_dictionary returns a dict."""
        self.assertEqual(type(Square(1).to_dictionary()), dict)

    def test_dictionary_roundtrip(self):
        """A dictionary can rebuild an identical square."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(s1.to_dictionary(), s2.to_dictionary())


class TestSquareSaveToFile(unittest.TestCase):
    """Tests for save_to_file when called on the Square class."""

    def setUp(self):
        """Remove any leftover Square.json before each test."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def tearDown(self):
        """Remove the Square.json created by a test."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_save_squares(self):
        """A list of squares is written to Square.json."""
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))

    def test_save_none_writes_empty_list(self):
        """Square.save_to_file(None) writes '[]' to Square.json."""
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty_list_writes_empty_list(self):
        """Square.save_to_file([]) writes '[]' to Square.json."""
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")


if __name__ == "__main__":
    unittest.main()
