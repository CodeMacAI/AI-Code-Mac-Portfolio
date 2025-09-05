# Script to calculate the square of a user-entered number with error handling
def calculate_square():
    while True:
        try:
            # Get user input and convert to float
            number = float(input("Enter a number to square: "))
            # Calculate the square
            square = number ** 2
            # Display the result
            print(f"The square of {number} is {square}")
            break  # Exit loop if successful
        except ValueError:
            # Display error message for non-numeric input
            print("Error: Please enter a valid number (e.g., 5 or 3.5). Try again.")

# Run the function
calculate_square()