# Function to calculate total cost of items
def calculate_total_cost():
    prices = []
    while True:
        try:
            # Get number of items
            num_items = int(input("Enter the number of items (or 0 to finish): "))
            if num_items == 0:
                break
            if num_items < 0:
                print("Error: Number of items cannot be negative. Try again.")
                continue
            # Get prices for each item
            for i in range(num_items):
                price = float(input(f"Enter price for item {i + 1}: £"))
                if price < 0:
                    print("Error: Price cannot be negative. Try again.")
                    i -= 1
                    continue
                prices.append(price)
            break
        except ValueError:
            print("Error: Please enter valid numbers. Try again.")
    # Calculate and display total
    total = sum(prices)
    if prices:
        print(f"Total cost for {len(prices)} items: £{total:.2f}")
    else:
        print("No items entered.")

# Run the function
calculate_total_cost()