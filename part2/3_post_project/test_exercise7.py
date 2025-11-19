"""
Tests for Exercise 7: Read Integers Until 'done'
"""
import unittest
from unittest.mock import patch
from io import StringIO
import exercise7


class TestExercise7(unittest.TestCase):
    """Test cases for exercise7 functions."""

    @patch('builtins.input', side_effect=['10', '20', '30', 'done'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_valid_integers(self, mock_stdout, mock_input):
        """Test main function with valid integers."""
        exercise7.main()
        output = mock_stdout.getvalue()
        self.assertIn("Total: 60", output)
        self.assertIn("Count: 3", output)
        self.assertIn("Average: 20", output)

    @patch('builtins.input', side_effect=['5', '15', '25', 'done'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_average_calculation(self, mock_stdout, mock_input):
        """Test main function average calculation."""
        exercise7.main()
        output = mock_stdout.getvalue()
        self.assertIn("Total: 45", output)
        self.assertIn("Average: 15", output)

    @patch('builtins.input', side_effect=['done'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_no_numbers(self, mock_stdout, mock_input):
        """Test main function with no numbers entered."""
        exercise7.main()
        output = mock_stdout.getvalue()
        self.assertIn("Total: 0", output)
        self.assertIn("Count: 0", output)
        self.assertIn("N/A", output)

    @patch('builtins.input', side_effect=['10', 'abc', '20', 'xyz', '30', 'done'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_invalid_inputs(self, mock_stdout, mock_input):
        """Test main function with invalid inputs."""
        exercise7.main()
        output = mock_stdout.getvalue()
        self.assertIn("Total: 60", output)
        self.assertIn("Count: 3", output)
        self.assertIn("Error", output)

    @patch('builtins.input', side_effect=['-5', '10', '-15', 'done'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_negative_integers(self, mock_stdout, mock_input):
        """Test main function with negative integers."""
        exercise7.main()
        output = mock_stdout.getvalue()
        self.assertIn("Total: -10", output)
        self.assertIn("Count: 3", output)

    @patch('builtins.input', side_effect=['DONE'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_done_uppercase(self, mock_stdout, mock_input):
        """Test main function with uppercase DONE."""
        exercise7.main()
        output = mock_stdout.getvalue()
        self.assertIn("Total: 0", output)
        self.assertIn("Count: 0", output)


if __name__ == '__main__':
    unittest.main()

