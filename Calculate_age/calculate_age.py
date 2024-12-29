# Function to calculate age
def calculate_age(birth_year, current_year):
    age = current_year - birth_year
    return age

# Taking user input for birth year/item creation year and current year
birth_year = int(input("Enter the year the person/item was born/created: "))
current_year = int(input("Enter the current year: "))

# Calculate the age
age = calculate_age(birth_year, current_year)

# Output the result
print(f"The age of the person/item is: {age} years.")
