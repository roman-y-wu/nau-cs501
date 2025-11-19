"""
Tests for Exercise 2: Population Growth Comparison Program
"""
import unittest
from unittest.mock import patch
from io import StringIO
import exercise2


class TestExercise2(unittest.TestCase):
    """Test cases for exercise2 functions."""

    def test_get_growth(self):
        """Test get_growth function."""
        self.assertEqual(exercise2.get_growth(1000, 0.03), 1030.0)
        self.assertEqual(exercise2.get_growth(5000, 0.05), 5250.0)
        self.assertAlmostEqual(exercise2.get_growth(10000, 0.025), 10250.0, places=2)

    def test_check_data_valid(self):
        """Test check_data with valid inputs."""
        self.assertTrue(exercise2.check_data(1000, 2000, 0.05, 0.02))

    def test_check_data_invalid_population_zero(self):
        """Test check_data with zero population."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(exercise2.check_data(0, 2000, 0.05, 0.02))
            self.assertIn("Populations must be greater than zero", mock_stdout.getvalue())

    def test_check_data_invalid_rate_zero(self):
        """Test check_data with zero growth rate."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(exercise2.check_data(1000, 2000, 0, 0.02))
            self.assertIn("Growth rates must be greater than zero", mock_stdout.getvalue())

    def test_check_data_invalid_population_a_too_large(self):
        """Test check_data when population A >= population B."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(exercise2.check_data(2000, 2000, 0.05, 0.02))
            self.assertIn("Population of city A must be smaller", mock_stdout.getvalue())

    def test_check_data_invalid_rate_a_too_small(self):
        """Test check_data when rate A <= rate B."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(exercise2.check_data(1000, 2000, 0.02, 0.05))
            self.assertIn("Growth rate of city A must be greater", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['1000', '2000', '5', '2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_valid_input(self, mock_stdout, mock_input):
        """Test main function with valid inputs."""
        exercise2.main()
        output = mock_stdout.getvalue()
        self.assertIn("Number of years", output)
        self.assertIn("Final population", output)


if __name__ == '__main__':
    unittest.main()

