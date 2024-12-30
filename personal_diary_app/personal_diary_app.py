import os
from datetime import datetime

# Function to write the diary entry to the file
def write_entry(filename):
    try:
        with open(filename, "a") as file:
            print("Enter your diary entry (type 'exit' to stop): ")
            while True:
                entry = input()
                if entry.lower() == 'exit':
                    break
                # Write the current date and entry to the file
                current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{current_date} - {entry}\n")
            print("Your entry has been saved.")
    except PermissionError:
        print("Permission denied. You don't have the rights to write to this file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to read all previous diary entries
def read_entries(filename):
    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                entries = file.read()
                if entries:
                    print("\nPrevious Entries:")
                    print(entries)
                else:
                    print("No entries found.")
        else:
            print("No diary entries found. Start by writing your first entry.")
    except FileNotFoundError:
        print("The diary file could not be found.")
    except PermissionError:
        print("Permission denied. You don't have the rights to read this file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function for the diary application
def main():
    filename = "diary.txt"
    
    while True:
        print("\nWelcome to your Personal Diary!")
        print("1. Write a new entry")
        print("2. View previous entries")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            write_entry(filename)
        elif choice == "2":
            read_entries(filename)
        elif choice == "3":
            print("Goodbye! Have a nice day!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
