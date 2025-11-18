"""
Exercise 6: Pythagorean Theorem Function

Write a function in Python with the following signature:
    pythagoreanTheorem(length_a, length_b)
The function returns the length of the hypotenuse assuming that length_a
and length_b are the lengths of the two legs of a right triangle.
"""

import math


def pythagoreanTheorem(length_a, length_b):
    """
    Calculate the length of the hypotenuse of a right triangle.

    Args:
        length_a (float): Length of the first leg of the triangle.
        length_b (float): Length of the second leg of the triangle.

    Returns:
        float: Length of the hypotenuse.
    """
    return math.hypot(length_a, length_b)


def main():
    """
    Main function to demonstrate pythagoreanTheorem with sample values
    and user input.
    """
    # Example calls
    print("Example calls:")
    print(f"pythagoreanTheorem(3, 4) = {pythagoreanTheorem(3, 4)}")
    print(f"pythagoreanTheorem(5, 12) = {pythagoreanTheorem(5, 12)}")
    print(f"pythagoreanTheorem(7, 24) = {pythagoreanTheorem(7, 24)}")

    # Optional user input
    print("\nNow you can enter your own values.")
    try:
        a = float(input("Enter length_a: "))
        b = float(input("Enter length_b: "))
    except ValueError:
        print("Error: Please enter valid numeric values.")
        return

    hyp = pythagoreanTheorem(a, b)
    print(f"The hypotenuse length is: {hyp}")


if __name__ == "__main__":
    main()


