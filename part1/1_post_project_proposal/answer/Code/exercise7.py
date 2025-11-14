"""
Exercise 7: University Grading System Program
Calculate average grade from two scores and determine the letter grade
"""


def get_grade(score):
    """
    Determine the letter grade based on the score
    
    Args:
        score: The average score (float)
    
    Returns:
        tuple: (letter_grade, is_failed)
    """
    if score < 30:
        return "F", True
    elif 30 <= score < 40:
        return "E", True
    elif 40 <= score < 50:
        return "D", False
    elif 50 <= score < 65:
        return "C", False
    elif 65 <= score <= 80:
        return "B", False
    else:  # score > 80
        return "A", False


def main():
    """
    Main function: Get two scores, validate them, calculate average,
    determine grade, and display the result
    """
    # Get first score
    score1 = float(input("Enter first score (0-100): "))
    
    # Validate first score
    if score1 < 0 or score1 > 100:
        print("Error: Score must be between 0 and 100.")
        return
    
    # Get second score
    score2 = float(input("Enter second score (0-100): "))
    
    # Validate second score
    if score2 < 0 or score2 > 100:
        print("Error: Score must be between 0 and 100.")
        return
    
    # Calculate average of the two scores
    average_score = (score1 + score2) / 2
    
    # Get letter grade and failure status
    letter_grade, is_failed = get_grade(average_score)
    
    # Display results
    print(f"\nFirst score: {score1:.2f}")
    print(f"Second score: {score2:.2f}")
    print(f"Average score: {average_score:.2f}")
    print(f"Grade: {letter_grade}")
    
    # If failed, inform the user
    if is_failed:
        print("Status: Failed")


if __name__ == "__main__":
    main()

