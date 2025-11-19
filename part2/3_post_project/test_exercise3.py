"""
Tests for Exercise 3: List Values Doubling Function
"""
import unittest
from unittest.mock import patch
from io import StringIO
import exercise3


class TestExercise3(unittest.TestCase):
    """Test cases for exercise3 functions."""

    def test_double_values_integers(self):
        """Test double_values with integer list."""
        self.assertEqual(exercise3.double_values([1, 2, 3]), [2, 4, 6])
        self.assertEqual(exercise3.double_values([0, 5, 10]), [0, 10, 20])

    def test_double_values_floats(self):
        """Test double_values with float list."""
        self.assertEqual(exercise3.double_values([1.5, 2.5, 3.5]), [3.0, 5.0, 7.0])
        self.assertEqual(exercise3.double_values([0.5, 1.0]), [1.0, 2.0])

    def test_double_values_mixed(self):
        """Test double_values with mixed int/float list."""
        result = exercise3.double_values([1, 2.5, 3])
        self.assertEqual(result, [2, 5.0, 6])

    def test_double_values_empty(self):
        """Test double_values with empty list."""
        self.assertEqual(exercise3.double_values([]), [])

    def test_double_values_negative(self):
        """Test double_values with negative numbers."""
        self.assertEqual(exercise3.double_values([-1, -2, 3]), [-2, -4, 6])

    @patch('builtins.input', return_value='1 2 3 4 5')
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_valid_input(self, mock_stdout, mock_input):
        """Test main function with valid input."""
        exercise3.main()
        output = mock_stdout.getvalue()
        self.assertIn("Original list", output)
        self.assertIn("Doubled list", output)
        self.assertIn("[2.0, 4.0, 6.0, 8.0, 10.0]", output)

    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_empty_input(self, mock_stdout, mock_input):
        """Test main function with empty input."""
        exercise3.main()
        output = mock_stdout.getvalue()
        self.assertIn("No numbers entered", output)


if __name__ == '__main__':
    unittest.main()

