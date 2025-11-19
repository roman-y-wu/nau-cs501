"""
Tests for Exercise 10: Country Dictionary Operations
"""
import unittest
import exercise10


class TestExercise10(unittest.TestCase):
    """Test cases for exercise10 functions."""

    def test_add_country(self):
        """Test add_country function."""
        countries = {}
        exercise10.add_country(countries, "France", 67_000_000, "French", "Europe")
        self.assertIn("France", countries)
        self.assertEqual(countries["France"]["population"], 67_000_000)
        self.assertEqual(countries["France"]["first_language"], "French")
        self.assertEqual(countries["France"]["continent"], "Europe")

    def test_add_currency_key(self):
        """Test add_currency_key function."""
        countries = {
            "USA": {"population": 328_000_000, "first_language": "English", "continent": "North America"}
        }
        exercise10.add_currency_key(countries)
        self.assertIn("currency", countries["USA"])
        self.assertEqual(countries["USA"]["currency"], "N/A")

    def test_add_currency_key_custom_default(self):
        """Test add_currency_key with custom default value."""
        countries = {
            "USA": {"population": 328_000_000, "first_language": "English", "continent": "North America"}
        }
        exercise10.add_currency_key(countries, "USD")
        self.assertEqual(countries["USA"]["currency"], "USD")

    def test_add_currency_key_multiple_countries(self):
        """Test add_currency_key with multiple countries."""
        countries = {
            "USA": {"population": 328_000_000, "first_language": "English", "continent": "North America"},
            "Brazil": {"population": 211_000_000, "first_language": "Portuguese", "continent": "South America"}
        }
        exercise10.add_currency_key(countries)
        self.assertIn("currency", countries["USA"])
        self.assertIn("currency", countries["Brazil"])
        self.assertEqual(countries["USA"]["currency"], "N/A")
        self.assertEqual(countries["Brazil"]["currency"], "N/A")

    def test_find_largest_population(self):
        """Test find_largest_population function."""
        countries = {
            "USA": {"population": 328_000_000, "first_language": "English", "continent": "North America"},
            "Brazil": {"population": 211_000_000, "first_language": "Portuguese", "continent": "South America"},
            "China": {"population": 1_393_000_000, "first_language": "Mandarin", "continent": "Asia"}
        }
        result = exercise10.find_largest_population(countries)
        self.assertIsNotNone(result)
        largest_name, largest_data = result
        self.assertEqual(largest_name, "China")
        self.assertEqual(largest_data["population"], 1_393_000_000)

    def test_find_largest_population_empty(self):
        """Test find_largest_population with empty dictionary."""
        countries = {}
        result = exercise10.find_largest_population(countries)
        self.assertIsNone(result)

    def test_find_largest_population_single_country(self):
        """Test find_largest_population with single country."""
        countries = {
            "USA": {"population": 328_000_000, "first_language": "English", "continent": "North America"}
        }
        result = exercise10.find_largest_population(countries)
        self.assertIsNotNone(result)
        largest_name, _ = result
        self.assertEqual(largest_name, "USA")

    def test_integration_all_functions(self):
        """Test integration of all three functions."""
        countries = {
            "USA": {"population": 328_000_000, "first_language": "English", "continent": "North America"}
        }
        
        # Add a country
        exercise10.add_country(countries, "India", 1_366_000_000, "Hindi", "Asia")
        self.assertIn("India", countries)
        
        # Add currency key
        exercise10.add_currency_key(countries, "N/A")
        self.assertIn("currency", countries["USA"])
        self.assertIn("currency", countries["India"])
        
        # Find largest population
        result = exercise10.find_largest_population(countries)
        largest_name, _ = result
        self.assertEqual(largest_name, "India")


if __name__ == '__main__':
    unittest.main()

