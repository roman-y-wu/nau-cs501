"""
Exercise 3: List Values Doubling Function
Write a Python function that takes as a parameter a list of numbers and returns
a list whose values are twice the values of the initial list.
"""


def double_values(numbers):
    """
    Return a new list where each element is twice the corresponding
    element of the input list.

    Args:
        numbers (list[float | int]): List of numeric values.

    Returns:
        list[float | int]: New list with each value doubled.
    """
    return [value * 2 for value in numbers]


def main():
    """
    Main function to demonstrate double_values:
    - Ask the user to enter numbers separated by spaces.
    - Convert the input into a list of floats.
    - Call double_values and display the original and resulting lists.
    """
    raw = input("Enter a list of numbers separated by spaces: ").strip()

    if not raw:
        print("No numbers entered.")
        return

    try:
        numbers = [float(part) for part in raw.split()]
    except ValueError:
        print("Error: Please enter only valid numeric values.")
        return

    doubled = double_values(numbers)

    print(f"Original list: {numbers}")
    print(f"Doubled list:  {doubled}")


if __name__ == "__main__":
    main()


