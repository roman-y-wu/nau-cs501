"""
Exercise 1: Total House Area Calculation Program
Calculate the total area of a house, assuming all rooms are rectangular.
"""


def get_area(width, length):
    """
    Calculate the area of a rectangular room.

    Args:
        width (float): Width of the room in meters.
        length (float): Length of the room in meters.

    Returns:
        float: Area of the room in square meters.
    """
    return width * length


def get_positive_float(prompt):
    """
    Ask the user for a positive real number and validate the input.

    Args:
        prompt (str): Message to display to the user.

    Returns:
        float: A positive real number entered by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: The value must be greater than zero. Please try again.\n")
            else:
                return value
        except ValueError:
            print("Error: Invalid number. Please enter a valid real number.\n")


def get_yes_no(prompt):
    """
    Ask the user a Yes/No question and validate the answer.

    Args:
        prompt (str): Message to display to the user.

    Returns:
        str: 'Y' for yes or 'N' for no.
    """
    while True:
        answer = input(prompt).strip().upper()
        if answer in ("Y", "N"):
            return answer
        print("Error: Please enter 'Y' for Yes or 'N' for No.\n")


def main():
    """
    Main function:
    - Repeatedly ask for room dimensions (width and length).
    - Calculate each room's area using get_area.
    - Sum the areas until the user chooses to stop.
    - Finally, display the total area of the house.
    """
    total_area = 0.0

    while True:
        print("\nEnter room measurements (in meters):")
        width = get_positive_float("  Width of the room: ")
        length = get_positive_float("  Length of the room: ")

        room_area = get_area(width, length)
        total_area += room_area

        print(f"  Area of this room: {room_area:.2f} square meters")

        continue_answer = get_yes_no("Do you want to enter another room? (Y/N): ")
        if continue_answer == "N":
            break

    print(f"\nThe total area of the house is: {total_area:.2f} square meters")


if __name__ == "__main__":
    main()


