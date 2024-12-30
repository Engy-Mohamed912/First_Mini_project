# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Get input from the user
try:
    num = int(input("Enter a number to calculate its factorial: "))
    
    # Check if the number is negative
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        # Calculate and print the factorial
        result = factorial(num)
        print(f"The factorial of {num} is {result}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
