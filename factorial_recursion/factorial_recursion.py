def factorial(n):
    # Base case: If n is 0 or 1, the factorial is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: factorial(n) = n * factorial(n-1)
        return n * factorial(n - 1)

# Example usage:
num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")
