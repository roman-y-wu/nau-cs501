"""
Exercise 5: Savings Account Interest Calculation Program
Calculate the balance of a savings account after one month with monthly interest rate
"""


def main():
    """
    Main function: Get current balance, calculate interest and new balance
    after one month, then display the results
    """
    # Get current balance of savings account
    current_balance = float(input("Enter current balance of your savings account: "))
    
    # Monthly interest rate (0.7%)
    monthly_interest_rate = 0.007
    
    # Calculate interest earned
    interest_earned = current_balance * monthly_interest_rate
    
    # Calculate balance after one month
    balance_after_one_month = current_balance + interest_earned
    
    # Display results
    print(f"\nCurrent balance: ${current_balance:.2f}")
    print(f"Monthly interest rate: {monthly_interest_rate * 100}%")
    print(f"Interest earned: ${interest_earned:.2f}")
    print(f"Balance after one month: ${balance_after_one_month:.2f}")


if __name__ == "__main__":
    main()

