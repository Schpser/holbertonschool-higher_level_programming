#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_normal_list(self):
        """Test with normal list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-5, -3, -1, -4]), -1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-10, 0, 10, -5]), 10)

    def test_single_element(self):
        """Test with list containing single element"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-3]), -3)

    def test_empty_list(self):
        """Test with empty list"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_duplicate_max(self):
        """Test with duplicate maximum values"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)
        self.assertEqual(max_integer([5, 2, 5, 1]), 5)

    def test_float_numbers(self):
        """Test with float numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 3.1, 2.0]), 3.1)
        self.assertEqual(max_integer([-1.5, -2.7, -3.1]), -1.5)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)
        self.assertEqual(max_integer([-1000000, -999999, -1000001]), -999999)

    def test_strings_in_list(self):
        """Test that TypeError is raised with strings in list"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3", 4])

    def test_none_in_list(self):
        """Test that TypeError is raised with None in list"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, None, 4])

    def test_no_arguments(self):
        """Test with no arguments (uses default empty list)"""
        self.assertIsNone(max_integer())

    def test_max_at_beginning(self):
        """Test with max at beginning of list"""
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_at_end(self):
        """Test with max at end of list"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_max_in_middle(self):
        """Test with max in middle of list"""
        self.assertEqual(max_integer([1, 10, 3, 4]), 10)


if __name__ == '__main__':
    unittest.main()
