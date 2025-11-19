"""
Tests for Exercise 1: Total House Area Calculation Program
"""
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import sys
import exercise1


class TestExercise1(unittest.TestCase):
    """Test cases for exercise1 functions."""

    def test_get_area(self):
        """Test get_area function with various inputs."""
        self.assertEqual(exercise1.get_area(5.0, 4.0), 20.0)
        self.assertEqual(exercise1.get_area(3.5, 2.5), 8.75)
        self.assertEqual(exercise1.get_area(10, 10), 100)
        self.assertEqual(exercise1.get_area(0.5, 0.5), 0.25)

    @patch('builtins.input', side_effect=['5.0'])
    def test_get_positive_float_valid(self, mock_input):
        """Test get_positive_float with valid input."""
        result = exercise1.get_positive_float("Enter width: ")
        self.assertEqual(result, 5.0)

    @patch('builtins.input', side_effect=['-5', '0', 'abc', '3.5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_positive_float_invalid_then_valid(self, mock_stdout, mock_input):
        """Test get_positive_float with invalid inputs then valid."""
        result = exercise1.get_positive_float("Enter width: ")
        self.assertEqual(result, 3.5)
        output = mock_stdout.getvalue()
        self.assertIn("Error", output)

    @patch('builtins.input', side_effect=['Y'])
    def test_get_yes_no_yes(self, mock_input):
        """Test get_yes_no with 'Y'."""
        result = exercise1.get_yes_no("Continue? ")
        self.assertEqual(result, 'Y')

    @patch('builtins.input', side_effect=['N'])
    def test_get_yes_no_no(self, mock_input):
        """Test get_yes_no with 'N'."""
        result = exercise1.get_yes_no("Continue? ")
        self.assertEqual(result, 'N')

    @patch('builtins.input', side_effect=['invalid', 'maybe', 'y'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_yes_no_invalid_then_valid(self, mock_stdout, mock_input):
        """Test get_yes_no with invalid inputs then valid."""
        result = exercise1.get_yes_no("Continue? ")
        self.assertEqual(result, 'Y')
        output = mock_stdout.getvalue()
        self.assertIn("Error", output)

    @patch('builtins.input', side_effect=['5.0', '4.0', 'N'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_single_room(self, mock_stdout, mock_input):
        """Test main function with a single room."""
        exercise1.main()
        output = mock_stdout.getvalue()
        self.assertIn("20.00 square meters", output)
        self.assertIn("total area", output.lower())

    @patch('builtins.input', side_effect=['3.0', '4.0', 'Y', '2.0', '2.0', 'N'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_multiple_rooms(self, mock_stdout, mock_input):
        """Test main function with multiple rooms."""
        exercise1.main()
        output = mock_stdout.getvalue()
        self.assertIn("12.00", output)  # First room area
        self.assertIn("4.00", output)   # Second room area
        self.assertIn("16.00", output)  # Total area


if __name__ == '__main__':
    unittest.main()

