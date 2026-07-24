#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function"""

    def test_ordered_list(self):
        """Max is the last element of an ascending list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max is found in an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        """Max is the first element of a descending list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """A single-element list returns that element"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """An empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """Calling with no argument returns None"""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Max works with only negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_sign_numbers(self):
        """Max works with a mix of negative and positive numbers"""
        self.assertEqual(max_integer([-10, 0, 10, 5]), 10)

    def test_duplicate_max(self):
        """Max is returned even if it appears more than once"""
        self.assertEqual(max_integer([3, 7, 7, 2]), 7)

    def test_all_same_values(self):
        """A list where every value is the same"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_max_at_start(self):
        """Max is the first element"""
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_end(self):
        """Max is the last element"""
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_floats(self):
        """Max works with a list of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_does_not_mutate_list(self):
        """The original list is left unchanged"""
        my_list = [1, 2, 3]
        max_integer(my_list)
        self.assertEqual(my_list, [1, 2, 3])

    def test_two_elements(self):
        """A two-element list returns the bigger one"""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)


if __name__ == '__main__':
    unittest.main()
