"""
Exercise 1: Store Discount Calculation Program
Calculate the total amount the salesperson should collect from the customer
"""


def main():
    """
    Main function: Get user input, calculate amounts before and after discount,
    and display the results
    """
    # Get product unit price
    product_value = float(input("Enter product unit price: "))
    
    # Get purchase quantity
    quantity = int(input("Enter purchase quantity: "))
    
    # Get discount percentage
    discount_percentage = float(input("Enter discount percentage (e.g., 10 for 10%): "))
    
    # Calculate total amount before discount
    total_before_discount = product_value * quantity
    
    # Calculate discount amount
    discount_amount = total_before_discount * (discount_percentage / 100)
    
    # Calculate final amount after discount
    final_amount = total_before_discount - discount_amount
    
    # Display results
    print(f"\nTotal amount before discount: ${total_before_discount:.2f}")
    print(f"Discount percentage: {discount_percentage}%")
    print(f"Discount amount: ${discount_amount:.2f}")
    print(f"Final amount to pay: ${final_amount:.2f}")


if __name__ == "__main__":
    main()
