"""
Exercise 2: Population Growth Comparison Program
Calculate and display the number of years required for the population of
city A to exceed or equal the population of city B, given the populations
and annual growth rates of the two cities.
"""


def get_growth(population, rate):
    """
    Calculate the new population after one year of growth.

    Args:
        population (float): Current population of the city.
        rate (float): Annual growth rate (as a decimal, e.g., 0.03 for 3%).

    Returns:
        float: Population after one year of growth.
    """
    return population + (population * rate)


def check_data(population_a, population_b, rate_a, rate_b):
    """
    Validate populations and growth rates for cities A and B.

    Conditions:
    - Populations of A and B must be greater than zero.
    - Growth rates of A and B must be greater than zero.
    - Population of A must be smaller than population of B.
    - Growth rate of A must be greater than growth rate of B.

    Args:
        population_a (float): Initial population of city A.
        population_b (float): Initial population of city B.
        rate_a (float): Annual growth rate of city A (decimal).
        rate_b (float): Annual growth rate of city B (decimal).

    Returns:
        bool: True if data is valid, False otherwise.
    """
    if population_a <= 0 or population_b <= 0:
        print("Error: Populations must be greater than zero.")
        return False

    if rate_a <= 0 or rate_b <= 0:
        print("Error: Growth rates must be greater than zero.")
        return False

    if population_a >= population_b:
        print("Error: Population of city A must be smaller than population of city B.")
        return False

    if rate_a <= rate_b:
        print("Error: Growth rate of city A must be greater than growth rate of city B.")
        return False

    return True


def main():
    """
    Main function:
    - Get populations and growth rates for cities A and B.
    - Validate the input data with check_data.
    - If valid, compute how many years it takes for A's population
      to reach or exceed B's population using get_growth.
    - Display the number of years and final populations.
    """
    print("Population Growth Comparison")

    try:
        population_a = float(input("Enter initial population of city A: "))
        population_b = float(input("Enter initial population of city B: "))

        rate_a_percent = float(
            input("Enter annual growth rate of city A (e.g., 3 for 3%): ")
        )
        rate_b_percent = float(
            input("Enter annual growth rate of city B (e.g., 1.5 for 1.5%): ")
        )
    except ValueError:
        print("Error: Please enter valid numeric values for populations and rates.")
        return

    # Convert rates from percentages to decimals
    rate_a = rate_a_percent / 100.0
    rate_b = rate_b_percent / 100.0

    if not check_data(population_a, population_b, rate_a, rate_b):
        # Invalid data; stop the program
        return

    years = 0

    # Iterate year by year until population of A >= population of B
    while population_a < population_b:
        population_a = get_growth(population_a, rate_a)
        population_b = get_growth(population_b, rate_b)
        years += 1

    print(
        f"\nNumber of years for city A's population to reach or exceed city B's: {years}"
    )
    print(f"Final population of city A: {population_a:.0f}")
    print(f"Final population of city B: {population_b:.0f}")


if __name__ == "__main__":
    main()


