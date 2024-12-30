def fibonacci(n):
    # Base case: when n is 0 or 1, return n
    if n <= 1:
        return n
    # Recursive case: sum of the previous two Fibonacci numbers
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
n = int(input("Enter a number: "))
print(f"The {n}-th Fibonacci number is: {fibonacci(n)}")
