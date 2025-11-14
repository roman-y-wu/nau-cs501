"""
Exercise 2: Basic Arithmetic Operations Program
Calculate sum, difference, product, and quotient of two integers
"""


def main():
    """
    Main function: Get two integers, calculate and display their sum,
    difference, product, and quotient
    """
    # Get first integer
    num1 = int(input("Enter first integer: "))
    
    # Get second integer
    num2 = int(input("Enter second integer: "))
    
    # Calculate sum
    sum_result = num1 + num2
    
    # Calculate difference
    difference = num1 - num2
    
    # Calculate product
    product = num1 * num2
    
    # Calculate quotient (check if divisor is zero)
    if num2 != 0:
        quotient = num1 / num2
        print(f"\nFirst number: {num1}")
        print(f"Second number: {num2}")
        print(f"Sum: {sum_result}")
        print(f"Difference: {difference}")
        print(f"Product: {product}")
        print(f"Quotient: {quotient:.2f}")
    else:
        print(f"\nFirst number: {num1}")
        print(f"Second number: {num2}")
        print(f"Sum: {sum_result}")
        print(f"Difference: {difference}")
        print(f"Product: {product}")
        print("Quotient: Error! Divisor cannot be zero")


if __name__ == "__main__":
    main()
