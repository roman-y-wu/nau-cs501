"""
Tests for Exercise 4: Remove Duplicates from a List
"""
import unittest
from unittest.mock import patch
from io import StringIO
import exercise4


class TestExercise4(unittest.TestCase):
    """Test cases for exercise4 functions."""

    def test_remove_duplicates_no_duplicates(self):
        """Test remove_duplicates with no duplicates."""
        self.assertEqual(exercise4.remove_duplicates([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_remove_duplicates_with_duplicates(self):
        """Test remove_duplicates with duplicates."""
        self.assertEqual(exercise4.remove_duplicates([1, 2, 2, 3, 3, 3, 4]), [1, 2, 3, 4])

    def test_remove_duplicates_strings(self):
        """Test remove_duplicates with strings."""
        self.assertEqual(exercise4.remove_duplicates(['a', 'b', 'a', 'c']), ['a', 'b', 'c'])

    def test_remove_duplicates_empty(self):
        """Test remove_duplicates with empty list."""
        self.assertEqual(exercise4.remove_duplicates([]), [])

    def test_remove_duplicates_all_same(self):
        """Test remove_duplicates with all same elements."""
        self.assertEqual(exercise4.remove_duplicates([1, 1, 1, 1]), [1])

    def test_remove_duplicates_preserves_order(self):
        """Test that remove_duplicates preserves order."""
        self.assertEqual(exercise4.remove_duplicates([3, 1, 3, 2, 1]), [3, 1, 2])

    @patch('builtins.input', return_value='apple banana apple cherry')
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_valid_input(self, mock_stdout, mock_input):
        """Test main function with valid input."""
        exercise4.main()
        output = mock_stdout.getvalue()
        self.assertIn("Original list", output)
        self.assertIn("Final list", output)
        self.assertIn("['apple', 'banana', 'cherry']", output)

    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_empty_input(self, mock_stdout, mock_input):
        """Test main function with empty input."""
        exercise4.main()
        output = mock_stdout.getvalue()
        self.assertIn("No items entered", output)


if __name__ == '__main__':
    unittest.main()

