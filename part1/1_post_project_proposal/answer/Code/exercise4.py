"""
Exercise 4: Student Grade Calculation Program
Calculate the average of three exam scores as the final grade
"""


def main():
    """
    Main function: Get three exam scores, calculate the average,
    and display the final grade
    """
    # Get first exam score
    score1 = float(input("Enter first exam score (0-100): "))
    
    # Get second exam score
    score2 = float(input("Enter second exam score (0-100): "))
    
    # Get third exam score
    score3 = float(input("Enter third exam score (0-100): "))
    
    # Calculate average (final grade)
    final_grade = (score1 + score2 + score3) / 3
    
    # Display results
    print(f"\nFirst exam score: {score1:.2f}")
    print(f"Second exam score: {score2:.2f}")
    print(f"Third exam score: {score3:.2f}")
    print(f"Final grade (average): {final_grade:.2f}")


if __name__ == "__main__":
    main()
