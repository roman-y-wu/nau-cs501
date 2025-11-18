"""
Exercise 4: Remove Duplicates from a List
Write a Python function that removes duplicate items from a list.
"""


def remove_duplicates(items):
    """
    Remove duplicate elements from a list while preserving the original order.

    Args:
        items (list): Input list containing possible duplicates.

    Returns:
        list: New list with duplicates removed.
    """
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


def main():
    """
    Main function to demonstrate remove_duplicates:
    - Ask the user to enter items separated by spaces.
    - Treat items as strings.
    - Show the list before and after removing duplicates.
    """
    raw = input("Enter list items separated by spaces: ").strip()

    if not raw:
        print("No items entered.")
        return

    items = raw.split()
    unique_items = remove_duplicates(items)

    print(f"Original list: {items}")
    print(f"Final list:    {unique_items}")


if __name__ == "__main__":
    main()


