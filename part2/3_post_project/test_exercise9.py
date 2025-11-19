"""
Tests for Exercise 9: Check if All Rows in a 2D List Have the Same Size
"""
import unittest
import exercise9


class TestExercise9(unittest.TestCase):
    """Test cases for exercise9 functions."""

    def test_all_rows_same_size_true(self):
        """Test all_rows_same_size with same-sized rows."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertTrue(exercise9.all_rows_same_size(matrix))

    def test_all_rows_same_size_false(self):
        """Test all_rows_same_size with different-sized rows."""
        matrix = [[1, 2], [3, 4, 5], [6]]
        self.assertFalse(exercise9.all_rows_same_size(matrix))

    def test_all_rows_same_size_empty(self):
        """Test all_rows_same_size with empty matrix."""
        self.assertTrue(exercise9.all_rows_same_size([]))

    def test_all_rows_same_size_single_row(self):
        """Test all_rows_same_size with single row."""
        matrix = [[1, 2, 3]]
        self.assertTrue(exercise9.all_rows_same_size(matrix))

    def test_all_rows_same_size_single_element_rows(self):
        """Test all_rows_same_size with single-element rows."""
        matrix = [[1], [2], [3]]
        self.assertTrue(exercise9.all_rows_same_size(matrix))

    def test_all_rows_same_size_mixed_types(self):
        """Test all_rows_same_size with mixed types."""
        matrix = [['a', 'b'], ['c', 'd'], ['e', 'f']]
        self.assertTrue(exercise9.all_rows_same_size(matrix))

    def test_all_rows_same_size_example_a(self):
        """Test with example A from the code."""
        a = [[1, 3, 5], [2, 4, 6]]
        self.assertTrue(exercise9.all_rows_same_size(a))

    def test_all_rows_same_size_example_b(self):
        """Test with example B from the code."""
        b = [[1, 3], [2, 4, 6, 8]]
        self.assertFalse(exercise9.all_rows_same_size(b))


if __name__ == '__main__':
    unittest.main()

