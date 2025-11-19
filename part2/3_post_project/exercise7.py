"""
Exercise 7: Read Integers Until 'done'

Write a program which repeatedly reads integers until the user enters 'done'.
Once 'done' is entered, print out the total, count, and average of the numbers.
If the user enters anything other than an integer, print an error message and
skip to the next number.
"""


def main():
    """
    Main function:
    - Read user input repeatedly.
    - Accept integers and accumulate total and count.
    - Stop when user types 'done' (case-insensitive).
    - On non-integer input, print an error and continue.
    - At the end, print total, count, and average (if count > 0).
    """
    total = 0
    count = 0

    while True:
        user_input = input("Enter an integer or 'done' to finish: ").strip()

        if user_input.lower() == "done":
            break

        try:
            number = int(user_input)
        except ValueError:
            print("Error: Please enter a valid integer or 'done'.")
            continue

        # isinstance hint: variable is an int here
        if isinstance(number, int):
            total += number
            count += 1

    print("\nResults:")
    print(f"Total: {total}")
    print(f"Count: {count}")

    if count > 0:
        average = total / count
        print(f"Average: {average}")
    else:
        print("Average: N/A (no numbers were entered)")


if __name__ == "__main__":
    main()


