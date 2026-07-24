#!/usr/bin/python3
"""Unittests for the Base class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """Tests for how Base assigns the id attribute."""

    def test_auto_id_is_sequential(self):
        """Consecutive objects without an id get increasing ids."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_given_id_is_used(self):
        """An explicit id is stored unchanged."""
        self.assertEqual(Base(12).id, 12)

    def test_given_id_does_not_change_counter(self):
        """Passing an id must not bump the internal counter."""
        b1 = Base()
        Base(50)
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_id_zero(self):
        """Zero is a valid explicit id."""
        self.assertEqual(Base(0).id, 0)

    def test_negative_id(self):
        """A negative explicit id is kept as-is."""
        self.assertEqual(Base(-7).id, -7)

    def test_string_id(self):
        """A non-integer explicit id is kept as-is (no validation)."""
        self.assertEqual(Base("hello").id, "hello")


class TestBaseToJsonString(unittest.TestCase):
    """Tests for Base.to_json_string."""

    def test_none_returns_empty_brackets(self):
        """None yields the string '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list_returns_empty_brackets(self):
        """An empty list yields the string '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_single_dict(self):
        """A one-dict list becomes a JSON list string."""
        d = [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]
        self.assertEqual(type(Base.to_json_string(d)), str)

    def test_json_content_roundtrips(self):
        """The JSON string can be parsed back into the same data."""
        import json
        d = [{"id": 9, "width": 1, "height": 2, "x": 3, "y": 4}]
        self.assertEqual(json.loads(Base.to_json_string(d)), d)

    def test_returns_str_type(self):
        """The result is always a string."""
        self.assertEqual(type(Base.to_json_string([{"id": 1}])), str)


class TestBaseFromJsonString(unittest.TestCase):
    """Tests for Base.from_json_string."""

    def test_none_returns_empty_list(self):
        """None yields an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string_returns_empty_list(self):
        """An empty string yields an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_returns_list_type(self):
        """A JSON string is parsed into a list."""
        s = '[{"id": 1, "width": 2}]'
        self.assertEqual(type(Base.from_json_string(s)), list)

    def test_content_is_correct(self):
        """The parsed list matches the original dictionaries."""
        s = '[{"id": 1, "width": 2}, {"id": 3, "width": 4}]'
        self.assertEqual(
            Base.from_json_string(s),
            [{"id": 1, "width": 2}, {"id": 3, "width": 4}])


class TestBaseSaveToFile(unittest.TestCase):
    """Tests for Base.save_to_file."""

    def tearDown(self):
        """Remove any file created during a test."""
        for name in ("Rectangle.json", "Square.json", "Base.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_saves_rectangles(self):
        """Rectangles are written to Rectangle.json."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_none_writes_empty_list(self):
        """None writes '[]' to the file."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_empty_list_writes_empty_list(self):
        """An empty list writes '[]' to the file."""
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_overwrites_existing_file(self):
        """A second save replaces the previous content."""
        Rectangle.save_to_file([Rectangle(9, 9)])
        Rectangle.save_to_file([Rectangle(1, 1)])
        with open("Rectangle.json") as f:
            self.assertIn('"width": 1', f.read())

    def test_square_filename(self):
        """Squares are written to Square.json."""
        Square.save_to_file([Square(3)])
        self.assertTrue(os.path.exists("Square.json"))


class TestBaseLoadFromFile(unittest.TestCase):
    """Tests for Base.load_from_file."""

    def tearDown(self):
        """Remove any file created during a test."""
        for name in ("Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_missing_file_returns_empty_list(self):
        """A missing file yields an empty list."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_loads_rectangles(self):
        """Saved rectangles come back as Rectangle instances."""
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8)])
        loaded = Rectangle.load_from_file()
        self.assertEqual(type(loaded[0]), Rectangle)

    def test_loaded_values_match(self):
        """The loaded instance keeps the saved values."""
        r = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r])
        loaded = Rectangle.load_from_file()
        self.assertEqual(loaded[0].to_dictionary(), r.to_dictionary())

    def test_loads_squares(self):
        """Saved squares come back as Square instances."""
        Square.save_to_file([Square(5)])
        loaded = Square.load_from_file()
        self.assertEqual(type(loaded[0]), Square)


class TestBaseCreate(unittest.TestCase):
    """Tests for Base.create."""

    def test_create_rectangle_type(self):
        """create returns an instance of the calling class."""
        r = Rectangle.create(**{"id": 1, "width": 2, "height": 3})
        self.assertIsInstance(r, Rectangle)

    def test_create_rectangle_values(self):
        """create applies every attribute from the dictionary."""
        d = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        self.assertEqual(Rectangle.create(**d).to_dictionary(), d)

    def test_create_returns_new_object(self):
        """create returns a distinct object, not the original."""
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsNot(r1, r2)

    def test_create_square_type(self):
        """create builds a Square when called on Square."""
        s = Square.create(**{"id": 1, "size": 3})
        self.assertIsInstance(s, Square)

    def test_create_square_values(self):
        """create applies every attribute for a Square."""
        d = {"id": 1, "size": 3, "x": 4, "y": 5}
        self.assertEqual(Square.create(**d).to_dictionary(), d)


class TestBaseCsv(unittest.TestCase):
    """Tests for the CSV serialization helpers."""

    def tearDown(self):
        """Remove any file created during a test."""
        for name in ("Rectangle.csv", "Square.csv"):
            if os.path.exists(name):
                os.remove(name)

    def test_missing_rectangle_csv(self):
        """A missing Rectangle.csv yields an empty list."""
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        self.assertEqual(Rectangle.load_from_file_csv(), [])

    def test_rectangle_csv_roundtrip(self):
        """Rectangles survive a CSV save/load round-trip."""
        r = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file_csv([r])
        loaded = Rectangle.load_from_file_csv()
        self.assertEqual(loaded[0].to_dictionary(), r.to_dictionary())

    def test_rectangle_csv_type(self):
        """Loaded CSV rectangles are Rectangle instances."""
        Rectangle.save_to_file_csv([Rectangle(1, 2)])
        loaded = Rectangle.load_from_file_csv()
        self.assertEqual(type(loaded[0]), Rectangle)

    def test_square_csv_roundtrip(self):
        """Squares survive a CSV save/load round-trip."""
        s = Square(7, 9, 1, 6)
        Square.save_to_file_csv([s])
        loaded = Square.load_from_file_csv()
        self.assertEqual(loaded[0].to_dictionary(), s.to_dictionary())

    def test_square_csv_type(self):
        """Loaded CSV squares are Square instances."""
        Square.save_to_file_csv([Square(5)])
        loaded = Square.load_from_file_csv()
        self.assertEqual(type(loaded[0]), Square)


if __name__ == "__main__":
    unittest.main()
