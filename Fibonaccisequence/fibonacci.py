# Function to print Fibonacci sequence up to a given count
def fibonacci_sequence(count):
    # First two numbers of the Fibonacci sequence
    a, b = 0, 1

    # Print the Fibonacci sequence
    for _ in range(count):
        print(a, end=" ")  # Print the current number
        a, b = b, a + b  # Update a and b for the next numbers in the sequence

# Take input from the user for the count
count = int(input("Enter the number of Fibonacci terms to display: "))

# Print the Fibonacci sequence
fibonacci_sequence(count)
