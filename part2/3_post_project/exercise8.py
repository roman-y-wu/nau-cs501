"""
Exercise 8: Dictionary of Student Grades

Given the following dictionary (initial example):
    grades = {'John': 95, 'Paul': 84, 'Sam': 70, 'Tony': 35, 'Kate': 100}

Create a program that repeatedly asks the user to provide a name to be
queried in the dictionary.

Behavior:
    - If the name exists, ask the user if they want to:
        1. update the grade (ask for a new grade and update it), or
        2. delete the entry.
    - If the name does not exist, ask for a grade and add the new student.
    - If the user types EXIT instead of a name, exit the program.
    - List all the grades in the dictionary after each deletion, update,
      or inclusion (and before closing the program).
"""


def print_grades(grades):
    """
    Print all students and their grades in the dictionary.

    Args:
        grades (dict[str, int]): Dictionary of students and grades.
    """
    if not grades:
        print("No grades in the dictionary.")
        return

    print("Current grades:")
    for name, grade in grades.items():
        print(f"  {name}: {grade}")


def get_valid_grade(prompt):
    """
    Ask the user for a valid integer grade (0-100).

    Args:
        prompt (str): Prompt message for input.

    Returns:
        int: A valid grade between 0 and 100 (inclusive).
    """
    while True:
        try:
            grade = int(input(prompt))
        except ValueError:
            print("Error: Please enter an integer value for the grade.")
            continue

        if 0 <= grade <= 100:
            return grade

        print("Error: Grade must be between 0 and 100.")


def main():
    """
    Main function implementing interactive dictionary operations
    for student grades.
    """
    grades = {"John": 95, "Paul": 84, "Sam": 70, "Tony": 35, "Kate": 100}

    print("Initial grades:")
    print_grades(grades)

    while True:
        print("\nType a student name to query (or type 'EXIT' to quit).")
        name = input("Name: ").strip()

        if not name:
            print("Please enter a non-empty name.")
            continue

        if name.upper() == "EXIT":
            print("\nFinal grades before exiting:")
            print_grades(grades)
            break

        # Name exists in dictionary
        if name in grades:
            print(f"'{name}' found with grade {grades[name]}.")
            print("Choose an option:")
            print("  1 - Update the grade")
            print("  2 - Delete the entry")

            choice = input("Enter your choice (1 or 2): ").strip()

            if choice == "1":
                new_grade = get_valid_grade(f"Enter new grade for {name}: ")
                grades[name] = new_grade
                print(f"Grade for '{name}' updated to {new_grade}.")
            elif choice == "2":
                deleted_grade = grades.pop(name)
                print(f"Entry for '{name}' with grade {deleted_grade} deleted.")
            else:
                print("Invalid option. No changes made.")

        # Name does not exist
        else:
            print(f"'{name}' is not in the dictionary.")
            grade = get_valid_grade(f"Enter grade for new student {name}: ")
            grades[name] = grade
            print(f"Added '{name}' with grade {grade}.")

        # After each operation, list all grades
        print("\nUpdated list of grades:")
        print_grades(grades)


if __name__ == "__main__":
    main()


