import math  # Import the math module to access the value of pi

# Function to calculate area and circumference
def calculate_area_and_circumference(radius):
    # Area of the circle
    area = math.pi * radius ** 2
    
    # Circumference of the circle
    circumference = 2 * math.pi * radius
    
    return area, circumference

# Take input from the user for the radius
radius = float(input("Enter the radius of the circle: "))

# Calculate area and circumference
area, circumference = calculate_area_and_circumference(radius)

# Print the results
print(f"The area of the circle with radius {radius} is: {area:.2f}")
print(f"The circumference of the circle with radius {radius} is: {circumference:.2f}")
