# Function to check if a shop is open based on user-entered time
def is_shop_open():
    # Dictionary of shop names and their opening hours (from grimsby_shop_hours.py)
    shop_hours = {
        "Grimsby Fish Market": "8:00 AM - 5:00 PM",
        "Freshfields Farm Shop": "9:00 AM - 6:00 PM",
        "Tesco Grimsby": "7:00 AM - 10:00 PM",
        "Greggs Grimsby": "6:30 AM - 6:00 PM",
        "Wilko Grimsby": "8:00 AM - 8:00 PM"
    }

    # Get user input
    shop_name = input("Enter a shop name (e.g., Grimsby Fish Market): ").strip()
    if shop_name not in shop_hours:
        print("Shop not found. Please try again.")
        return

    time_input = input("Enter time to check (e.g., 2:00 PM): ").strip()
    try:
        # Simple time comparison (assumes 12-hour format with AM/PM)
        open_hour, close_hour = shop_hours[shop_name].split(" - ")
        if (time_input >= open_hour and time_input <= close_hour):
            print(f"{shop_name} is open at {time_input}.")
        else:
            print(f"{shop_name} is closed at {time_input}.")
    except ValueError:
        print("Error: Invalid time format. Use HH:MM AM/PM (e.g., 2:00 PM).")

# Run the function
is_shop_open()