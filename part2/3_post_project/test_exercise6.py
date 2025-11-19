"""
Tests for Exercise 6: Pythagorean Theorem Function
"""
import unittest
from unittest.mock import patch
from io import StringIO
import exercise6


class TestExercise6(unittest.TestCase):
    """Test cases for exercise6 functions."""

    def test_pythagoreanTheorem_3_4_5(self):
        """Test pythagoreanTheorem with classic 3-4-5 triangle."""
        result = exercise6.pythagoreanTheorem(3, 4)
        self.assertEqual(result, 5.0)

    def test_pythagoreanTheorem_5_12_13(self):
        """Test pythagoreanTheorem with 5-12-13 triangle."""
        result = exercise6.pythagoreanTheorem(5, 12)
        self.assertEqual(result, 13.0)

    def test_pythagoreanTheorem_7_24_25(self):
        """Test pythagoreanTheorem with 7-24-25 triangle."""
        result = exercise6.pythagoreanTheorem(7, 24)
        self.assertEqual(result, 25.0)

    def test_pythagoreanTheorem_floats(self):
        """Test pythagoreanTheorem with float inputs."""
        result = exercise6.pythagoreanTheorem(1.5, 2.0)
        self.assertAlmostEqual(result, 2.5, places=5)

    def test_pythagoreanTheorem_zero(self):
        """Test pythagoreanTheorem with zero."""
        result = exercise6.pythagoreanTheorem(0, 5)
        self.assertEqual(result, 5.0)

    def test_pythagoreanTheorem_same_lengths(self):
        """Test pythagoreanTheorem with equal leg lengths."""
        result = exercise6.pythagoreanTheorem(5, 5)
        self.assertAlmostEqual(result, 7.0710678118654755, places=5)

    @patch('builtins.input', side_effect=['3', '4'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_valid_input(self, mock_stdout, mock_input):
        """Test main function with valid input."""
        exercise6.main()
        output = mock_stdout.getvalue()
        self.assertIn("hypotenuse", output.lower())
        self.assertIn("5.0", output)


if __name__ == '__main__':
    unittest.main()

