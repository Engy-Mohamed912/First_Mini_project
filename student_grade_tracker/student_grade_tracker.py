import os

def read_grades_from_file(file_name):
    """Reads grades from the file and returns them as a list of integers."""
    grades = []
    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as file:
                for line in file:
                    try:
                        grades.append(int(line.strip()))  # Convert each line to an integer
                    except ValueError:
                        print(f"Warning: Invalid grade found in file, skipping: {line.strip()}")
        except IOError:
            print("Error reading the file.")
    return grades


def write_grades_to_file(file_name, grades):
    """Writes grades to the file."""
    try:
        with open(file_name, "a") as file:  # Open file in append mode
            for grade in grades:
                file.write(f"{grade}\n")
        print("Grades have been successfully saved to the file.")
    except IOError:
        print("Error writing to the file.")


def calculate_average(grades):
    """Calculates and returns the average of the grades."""
    if not grades:
        return 0  # Avoid division by zero if the list is empty
    return sum(grades) / len(grades)


def input_grades():
    """Prompts the user to input grades."""
    grades = []
    while True:
        try:
            grade = input("Enter a grade (or type 'done' to finish): ")
            if grade.lower() == "done":
                break
            grade = int(grade)
            if grade < 0 or grade > 100:
                print("Please enter a grade between 0 and 100.")
            else:
                grades.append(grade)
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
    return grades


def main():
    file_name = "grades.txt"

    # Read existing grades from file
    grades = read_grades_from_file(file_name)

    # Allow the student to input new grades
    new_grades = input_grades()

    # Add new grades to the existing ones
    grades.extend(new_grades)

    # Save all grades to the file
    write_grades_to_file(file_name, new_grades)

    # Calculate and display the average
    if grades:
        average = calculate_average(grades)
        print(f"\nYour grades are: {grades}")
        print(f"Your average grade is: {average:.2f}")
    else:
        print("No grades available to calculate the average.")


if __name__ == "__main__":
    main()
