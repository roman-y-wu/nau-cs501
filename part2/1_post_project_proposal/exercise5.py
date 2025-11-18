"""
Exercise 5: Replace a Range of Elements in a List

Write a Python function that replaces a set of elements from a list between
indexes n and m (both inclusive) with a single element containing the string:
    "Elements from range n:m removed"
(replace n and m with the actual index values).

Before performing any operations, the function must check that n and m are
valid index values and print a message if they are invalid.

Note: Changes must be made in the list received by parameter and not in a
new variable.
"""


def replace_range_with_message(values, n, m):
    """
    Replace elements from index n to m (inclusive) with a single message string.

    This function modifies the list in-place, as required.

    Args:
        values (list): The list to be modified.
        n (int): Starting index of the range (inclusive).
        m (int): Ending index of the range (inclusive).

    Returns:
        None
    """
    length = len(values)

    # Validate indices
    if length == 0:
        print("Error: The list is empty; no elements can be replaced.")
        return

    if not (0 <= n < length) or not (0 <= m < length):
        print("Error: Indices n and m must be within the bounds of the list.")
        return

    if n > m:
        print("Error: Index n must be less than or equal to index m.")
        return

    # Build the message using the actual indices
    message = f"Elements from range {n}:{m} removed"

    # In-place replacement using slice assignment
    values[n : m + 1] = [message]


def main():
    """
    Main function to demonstrate replace_range_with_message:
    - Ask the user to enter list items separated by spaces.
    - Ask for indices n and m.
    - Call the function and display the list before and after.
    """
    raw = input("Enter list items separated by spaces: ").strip()

    if not raw:
        print("No items entered.")
        return

    values = raw.split()

    try:
        n = int(input("Enter starting index n (0-based): "))
        m = int(input("Enter ending index m (0-based): "))
    except ValueError:
        print("Error: Indices n and m must be integers.")
        return

    print(f"Original list: {values}")
    replace_range_with_message(values, n, m)
    print(f"Modified list: {values}")


if __name__ == "__main__":
    main()


