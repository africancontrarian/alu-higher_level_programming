#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import unittest
import io
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleInstantiation(unittest.TestCase):
    """Tests for creating Rectangle instances."""

    def test_is_base_subclass(self):
        """Rectangle inherits from Base."""
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_two_args(self):
        """Width and height are stored, x and y default to 0."""
        r = Rectangle(3, 4)
        self.assertEqual((r.width, r.height, r.x, r.y), (3, 4, 0, 0))

    def test_all_positional_args(self):
        """Every positional argument is stored on the right attribute."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(
            (r.width, r.height, r.x, r.y, r.id), (1, 2, 3, 4, 5))

    def test_auto_id(self):
        """An id is assigned automatically when omitted."""
        self.assertIsNotNone(Rectangle(1, 2).id)

    def test_missing_args_raises(self):
        """Width and height are required arguments."""
        with self.assertRaises(TypeError):
            Rectangle(1)


class TestRectangleWidth(unittest.TestCase):
    """Tests for the width validation."""

    def test_non_int_width(self):
        """A non-integer width raises TypeError."""
        with self.assertRaises(TypeError) as e:
            Rectangle("1", 2)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_float_width(self):
        """A float width raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1.5, 2)

    def test_zero_width(self):
        """A zero width raises ValueError."""
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_negative_width(self):
        """A negative width raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-3, 2)

    def test_bool_width(self):
        """A boolean width raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(True, 2)


class TestRectangleHeight(unittest.TestCase):
    """Tests for the height validation."""

    def test_non_int_height(self):
        """A non-integer height raises TypeError."""
        with self.assertRaises(TypeError) as e:
            Rectangle(1, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_zero_height(self):
        """A zero height raises ValueError."""
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 0)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_negative_height(self):
        """A negative height raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)


class TestRectangleXY(unittest.TestCase):
    """Tests for the x and y validation."""

    def test_non_int_x(self):
        """A non-integer x raises TypeError."""
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, "3")
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_negative_x(self):
        """A negative x raises ValueError."""
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, -3)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_non_int_y(self):
        """A non-integer y raises TypeError."""
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, "4")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_negative_y(self):
        """A negative y raises ValueError."""
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, 3, -4)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_zero_xy_allowed(self):
        """Zero is a valid x and y."""
        r = Rectangle(1, 2, 0, 0)
        self.assertEqual((r.x, r.y), (0, 0))


class TestRectangleArea(unittest.TestCase):
    """Tests for the area method."""

    def test_area(self):
        """Area is width times height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_area_large(self):
        """Area works with larger values."""
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_area_one(self):
        """A 1x1 rectangle has an area of 1."""
        self.assertEqual(Rectangle(1, 1).area(), 1)


class TestRectangleDisplay(unittest.TestCase):
    """Tests for the display method."""

    def test_display_simple(self):
        """A 2x2 rectangle prints two rows of two hashes."""
        r = Rectangle(2, 2)
        buf = io.StringIO()
        with redirect_stdout(buf):
            r.display()
        self.assertEqual(buf.getvalue(), "##\n##\n")

    def test_display_with_xy(self):
        """x and y produce leading spaces and blank lines."""
        r = Rectangle(2, 3, 2, 2)
        buf = io.StringIO()
        with redirect_stdout(buf):
            r.display()
        self.assertEqual(buf.getvalue(), "\n\n  ##\n  ##\n  ##\n")


class TestRectangleStr(unittest.TestCase):
    """Tests for the __str__ method."""

    def test_str(self):
        """__str__ follows the documented format."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_defaults(self):
        """__str__ uses the default x and y when they are omitted."""
        r = Rectangle(5, 5)
        self.assertEqual(str(r), "[Rectangle] ({}) 0/0 - 5/5".format(r.id))


class TestRectangleUpdateArgs(unittest.TestCase):
    """Tests for update with positional arguments."""

    def test_update_id(self):
        """The first positional argument is the id."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_all(self):
        """Positional arguments map to id, width, height, x, y."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_no_args_no_change(self):
        """Calling update with nothing leaves the object unchanged."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Tests for update with keyword arguments."""

    def test_update_single_kwarg(self):
        """A single keyword argument updates one attribute."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)

    def test_update_many_kwargs(self):
        """Several keyword arguments update several attributes."""
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/10")

    def test_args_take_priority(self):
        """kwargs are ignored when args are present."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, width=99)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 10)


class TestRectangleToDictionary(unittest.TestCase):
    """Tests for the to_dictionary method."""

    def test_dictionary_content(self):
        """The dictionary holds every expected key/value."""
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(
            r.to_dictionary(),
            {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_dictionary_type(self):
        """to_dictionary returns a dict."""
        self.assertEqual(type(Rectangle(1, 1).to_dictionary()), dict)

    def test_dictionary_roundtrip(self):
        """A dictionary can rebuild an identical rectangle."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())


if __name__ == "__main__":
    unittest.main()
