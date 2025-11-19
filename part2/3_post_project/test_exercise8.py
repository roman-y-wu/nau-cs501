"""
Tests for Exercise 8: Dictionary of Student Grades
"""
import unittest
from unittest.mock import patch
from io import StringIO
import exercise8


class TestExercise8(unittest.TestCase):
    """Test cases for exercise8 functions."""

    def test_print_grades_empty(self):
        """Test print_grades with empty dictionary."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            exercise8.print_grades({})
            output = mock_stdout.getvalue()
            self.assertIn("no grades", output.lower())

    def test_print_grades_non_empty(self):
        """Test print_grades with non-empty dictionary."""
        grades = {'John': 95, 'Paul': 84}
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            exercise8.print_grades(grades)
            output = mock_stdout.getvalue()
            self.assertIn("John: 95", output)
            self.assertIn("Paul: 84", output)

    @patch('builtins.input', side_effect=['100'])
    def test_get_valid_grade_valid(self, mock_input):
        """Test get_valid_grade with valid input."""
        result = exercise8.get_valid_grade("Enter grade: ")
        self.assertEqual(result, 100)

    @patch('builtins.input', side_effect=['-5', '101', 'abc', '85'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_valid_grade_invalid_then_valid(self, mock_stdout, mock_input):
        """Test get_valid_grade with invalid inputs then valid."""
        result = exercise8.get_valid_grade("Enter grade: ")
        self.assertEqual(result, 85)
        output = mock_stdout.getvalue()
        self.assertIn("Error", output)

    @patch('builtins.input', side_effect=['John', '1', '90', 'EXIT'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_update_grade(self, mock_stdout, mock_input):
        """Test main function updating a grade."""
        exercise8.main()
        output = mock_stdout.getvalue()
        self.assertIn("found with grade", output)
        self.assertIn("updated", output.lower())

    @patch('builtins.input', side_effect=['John', '2', 'EXIT'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_delete_entry(self, mock_stdout, mock_input):
        """Test main function deleting an entry."""
        exercise8.main()
        output = mock_stdout.getvalue()
        self.assertIn("deleted", output.lower())

    @patch('builtins.input', side_effect=['Alice', '88', 'EXIT'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_add_new_student(self, mock_stdout, mock_input):
        """Test main function adding a new student."""
        exercise8.main()
        output = mock_stdout.getvalue()
        self.assertIn("not in the dictionary", output)
        self.assertIn("Added", output)
        self.assertIn("Alice: 88", output)


if __name__ == '__main__':
    unittest.main()

