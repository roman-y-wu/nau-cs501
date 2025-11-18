"""
Exercise 10: Country Dictionary Operations

Given a dictionary of countries, create a program with the following
three functions:
    1. add a new country to the dictionary, using the same structure;
    2. add a new key to ALL entries called 'currency' and set all of them
       with 'N/A' (or a given default value);
    3. find the country with the largest population.
"""


def add_country(countries, name, population, first_language, continent):
    """
    Add a new country to the dictionary using the given structure.

    Args:
        countries (dict): Dictionary of countries.
        name (str): Country name (key).
        population (int): Population of the country.
        first_language (str): Main language.
        continent (str): Continent where the country is located.
    """
    countries[name] = {
        "population": population,
        "first_language": first_language,
        "continent": continent,
    }


def add_currency_key(countries, default_value="N/A"):
    """
    Add a 'currency' key to all countries in the dictionary.

    Args:
        countries (dict): Dictionary of countries.
        default_value (str): Default currency value to assign.
    """
    for data in countries.values():
        data["currency"] = default_value


def find_largest_population(countries):
    """
    Find the country with the largest population.

    Args:
        countries (dict): Dictionary of countries.

    Returns:
        tuple[str, dict] | None: (country_name, country_data) of the country
        with the largest population, or None if the dictionary is empty.
    """
    if not countries:
        return None

    # max with key function on population
    largest_country = max(
        countries.items(), key=lambda item: item[1].get("population", 0)
    )
    return largest_country


def print_countries(countries):
    """
    Helper function to display all countries and their data.
    """
    if not countries:
        print("No countries in the dictionary.")
        return

    for name, data in countries.items():
        print(f"{name}: {data}")


def main():
    """
    Main function demonstrating the three required operations.
    """
    countries = {
        "USA": {
            "population": 328_000_000,
            "first_language": "English",
            "continent": "North America",
        },
        "Brazil": {
            "population": 211_000_000,
            "first_language": "Portuguese",
            "continent": "South America",
        },
        "China": {
            "population": 1_393_000_000,
            "first_language": "Mandarin",
            "continent": "Asia",
        },
    }

    print("Initial dictionary:")
    print_countries(countries)

    # 1. Add a new country
    add_country(
        countries,
        name="Canada",
        population=37_600_000,
        first_language="English/French",
        continent="North America",
    )
    print("\nAfter adding Canada:")
    print_countries(countries)

    # 2. Add 'currency' key to all entries
    add_currency_key(countries)
    print("\nAfter adding 'currency' key to all countries:")
    print_countries(countries)

    # 3. Find the country with the largest population
    result = find_largest_population(countries)
    if result is not None:
        largest_name, largest_data = result
        print(
            f"\nCountry with the largest population: {largest_name} "
            f"({largest_data['population']})"
        )
    else:
        print("\nThe countries dictionary is empty.")


if __name__ == "__main__":
    main()


