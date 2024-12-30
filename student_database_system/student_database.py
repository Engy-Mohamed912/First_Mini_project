class Student:
    # Constructor to initialize the student attributes
    def __init__(self, name, age, grades):
        self.name = name  # Student's name
        self.age = age    # Student's age
        self.grades = grades  # List of grades

    # Method to display student information
    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {', '.join(map(str, self.grades))}")

    # Method to calculate the average grade
    def calculate_average_grade(self):
        if len(self.grades) == 0:  # Prevent division by zero
            return 0
        return sum(self.grades) / len(self.grades)

# Create instances of Student class
student1 = Student("Alice", 20, [88, 92, 78, 85])
student2 = Student("Bob", 22, [75, 84, 89, 91])
student3 = Student("Charlie", 21, [90, 94, 93, 87])

# Display student information and their average grades
students = [student1, student2, student3]

for student in students:
    student.display_student_info()
    print(f"Average Grade: {student.calculate_average_grade():.2f}\n")
