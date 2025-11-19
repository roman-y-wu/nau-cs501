"""
Exercise 9: Check if All Rows in a 2D List Have the Same Size

Write a Python function that takes a 2-dimensional list (a list of lists) as a
parameter and checks if all rows (sublists) have the same number of elements.
"""


def all_rows_same_size(matrix):
    """
    Check whether all rows in a 2D list have the same length.

    Args:
        matrix (list[list]): 2-dimensional list to check.

    Returns:
        bool: True if all rows have the same size, False otherwise.
    """
    if not matrix:
        # Empty matrix: we consider it as having consistent row sizes
        return True

    first_len = len(matrix[0])
    for row in matrix:
        if len(row) != first_len:
            return False
    return True


def main():
    """
    Main function to demonstrate all_rows_same_size with examples.
    """
    a = [
        [1, 3, 5],
        [2, 4, 6],
    ]

    b = [
        [1, 3],
        [2, 4, 6, 8],
    ]

    print("Matrix A:", a)
    print("Result:", all_rows_same_size(a))  # Expected: True

    print("\nMatrix B:", b)
    print("Result:", all_rows_same_size(b))  # Expected: False


if __name__ == "__main__":
    main()


