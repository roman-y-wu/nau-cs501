"""
Exercise 3: Salesperson Salary Calculation Program
Calculate total salary (basic salary + 8% sales commission)
"""


def main():
    """
    Main function: Get basic salary and total sales, calculate commission
    and total salary, then display the results
    """
    # Get salesperson's basic salary
    basic_salary = float(input("Enter salesperson's basic salary: "))
    
    # Get total sales for the month
    total_sales = float(input("Enter total sales for the month: "))
    
    # Calculate commission (8% of total sales)
    commission_rate = 0.08
    commission = total_sales * commission_rate
    
    # Calculate total salary (basic salary + commission)
    total_salary = basic_salary + commission
    
    # Display results
    print(f"\nBasic salary: ${basic_salary:.2f}")
    print(f"Total sales: ${total_sales:.2f}")
    print(f"Commission rate: {commission_rate * 100}%")
    print(f"Commission amount: ${commission:.2f}")
    print(f"Total salary: ${total_salary:.2f}")


if __name__ == "__main__":
    main()
