def calculate_average(numbers):
    if len(numbers) == 0:  # Check if the list is empty to avoid division by zero
        return 0  # Return 0 for empty list
    return sum(numbers) / len(numbers)  # Calculate and return the average

# Example usage
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("The average is:", average)
