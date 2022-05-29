#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """tests for 6-max_integer.py"""

    def test_list_integer(self):
        """Test for max at the end"""
        max_int = max_integer([1, 2, 3, 4])
        self.assertEqual(max_int, 4)

    def test_list_unordered_ints(self):
        """Test for max in the middle"""
        max_int = max_integer([1, 2, 4, 3])
        self.assertEqual(max_int, 4)

    def test_list_descend_order(self):
        """Test for max at the beginning"""
        max_int = max_integer([4, 2, 3, 1])
        self.assertEqual(max_int, 4)

    def test_max_at_begginning(self):
        """Test with negative numbers"""
        max_int = [-4, -3, -2, -1]
        self.assertEqual(max_integer(max_int), -1)

    def test_empty_list(self):
        """Test an empty list."""
        max_int = []
        self.assertEqual(max_integer(max_int), None)

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_string(self):
        """Test a string."""
        max_str = "List"
        self.assertEqual(max_integer(max_str), 't')

    def test_floats(self):
        """Test a list of floats."""
        max_int = [1.5, 2.5, 3.5, 4.5]
        self.assertEqual(max_integer(max_int), 4.5)

    def test_int_in_list(self):
        """Test one int in a list"""
        max_int_floats = [1.5, 2.5, 5, 3.5]
        self.assertEqual(max_integer(max_int_floats), 5)

    def test_list_one_element(self):
        """Test for list of one element"""
        max_int = [1]
        self.assertEqual(max_integer(max_int), 1)




if __name__ == '__main__':
    unittest.main()
