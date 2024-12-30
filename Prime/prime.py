# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to the square root of num
        if num % i == 0:
            return False
    return True

# Main program to print all primes between 2 and N
def print_primes_up_to_n(N):
    print(f"Prime numbers between 2 and {N} are:")
    for num in range(2, N + 1):  # Start from 2 up to N
        if is_prime(num):
            print(num, end=" ")

# Get user input
N = int(input("Enter a number N: "))
print_primes_up_to_n(N)
