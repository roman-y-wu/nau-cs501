"""
Tests for Exercise 5: Replace a Range of Elements in a List
"""
import unittest
from unittest.mock import patch
from io import StringIO
import exercise5


class TestExercise5(unittest.TestCase):
    """Test cases for exercise5 functions."""

    def test_replace_range_with_message_valid(self):
        """Test replace_range_with_message with valid indices."""
        values = ['a', 'b', 'c', 'd', 'e']
        exercise5.replace_range_with_message(values, 1, 3)
        self.assertEqual(values, ['a', 'Elements from range 1:3 removed', 'e'])

    def test_replace_range_with_message_single_element(self):
        """Test replace_range_with_message with single element range."""
        values = ['a', 'b', 'c']
        exercise5.replace_range_with_message(values, 1, 1)
        self.assertEqual(values, ['a', 'Elements from range 1:1 removed', 'c'])

    def test_replace_range_with_message_full_range(self):
        """Test replace_range_with_message with full range."""
        values = ['a', 'b', 'c']
        exercise5.replace_range_with_message(values, 0, 2)
        self.assertEqual(values, ['Elements from range 0:2 removed'])

    def test_replace_range_with_message_empty_list(self):
        """Test replace_range_with_message with empty list."""
        values = []
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            exercise5.replace_range_with_message(values, 0, 0)
            self.assertEqual(values, [])
            self.assertIn("empty", mock_stdout.getvalue().lower())

    def test_replace_range_with_message_invalid_index_n(self):
        """Test replace_range_with_message with invalid index n."""
        values = ['a', 'b', 'c']
        original = values.copy()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            exercise5.replace_range_with_message(values, 5, 2)
            self.assertEqual(values, original)  # Should not change
            self.assertIn("Error", mock_stdout.getvalue())

    def test_replace_range_with_message_invalid_index_m(self):
        """Test replace_range_with_message with invalid index m."""
        values = ['a', 'b', 'c']
        original = values.copy()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            exercise5.replace_range_with_message(values, 1, 5)
            self.assertEqual(values, original)  # Should not change
            self.assertIn("Error", mock_stdout.getvalue())

    def test_replace_range_with_message_n_greater_than_m(self):
        """Test replace_range_with_message when n > m."""
        values = ['a', 'b', 'c']
        original = values.copy()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            exercise5.replace_range_with_message(values, 2, 1)
            self.assertEqual(values, original)  # Should not change
            self.assertIn("Error", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['a b c d e', '1', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_valid_input(self, mock_stdout, mock_input):
        """Test main function with valid input."""
        exercise5.main()
        output = mock_stdout.getvalue()
        self.assertIn("Original list", output)
        self.assertIn("Modified list", output)


if __name__ == '__main__':
    unittest.main()

