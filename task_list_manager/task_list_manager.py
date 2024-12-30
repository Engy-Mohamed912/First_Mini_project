import os

# Define the filename to store the tasks
FILE_NAME = "tasks.txt"

# Function to read tasks from the file
def read_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    else:
        return []

# Function to save tasks to the file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to display the task list
def display_tasks(tasks):
    if tasks:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    else:
        print("No tasks found!")

# Function to add a task to the list
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added successfully!")

# Function to remove a task from the list
def remove_task(tasks):
    try:
        display_tasks(tasks)
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

# Main function to run the task manager
def run_task_manager():
    print("Welcome to the Task List Manager")
    tasks = read_tasks()

    while True:
        print("\nOptions:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the task manager
if __name__ == "__main__":
    try:
        run_task_manager()
    except Exception as e:
        print(f"An error occurred: {e}")
