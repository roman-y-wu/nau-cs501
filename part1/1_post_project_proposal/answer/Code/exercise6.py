"""
Exercise 6: Currency Conversion Program
Convert between British Pounds and US Dollars
"""


def main():
    """
    Main function: Get amount and currency type, convert to the other currency,
    and display the result
    """
    # Get amount to convert
    amount = float(input("Enter amount to convert: "))
    
    # Get original currency type
    print("Enter original currency type:")
    print("1. British Pounds (GBP)")
    print("2. US Dollars (USD)")
    currency_choice = input("Enter choice (1 or 2): ")
    
    # Exchange rate: 1.00 USD = 0.87 GBP
    # This means: 1 GBP = 1/0.87 USD ≈ 1.1494 USD
    usd_to_gbp_rate = 0.87
    gbp_to_usd_rate = 1 / usd_to_gbp_rate
    
    # Convert based on currency choice
    if currency_choice == "1":
        # Convert from GBP to USD
        converted_amount = amount * gbp_to_usd_rate
        print(f"\nOriginal amount: £{amount:.2f} (British Pounds)")
        print(f"Converted amount: ${converted_amount:.2f} (US Dollars)")
        print(f"Exchange rate: 1 GBP = {gbp_to_usd_rate:.4f} USD")
    elif currency_choice == "2":
        # Convert from USD to GBP
        converted_amount = amount * usd_to_gbp_rate
        print(f"\nOriginal amount: ${amount:.2f} (US Dollars)")
        print(f"Converted amount: £{converted_amount:.2f} (British Pounds)")
        print(f"Exchange rate: 1 USD = {usd_to_gbp_rate:.2f} GBP")
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()

