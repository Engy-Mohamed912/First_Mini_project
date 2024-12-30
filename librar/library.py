class Book:
    def __init__(self, title, author, is_available=True):
        # Initialize the book with title, author, and availability status
        self.title = title
        self.author = author
        self.is_available = is_available

    def check_out(self):
        # Check out the book if it's available
        if self.is_available:
            self.is_available = False
            print(f'You have successfully checked out "{self.title}".')
        else:
            print(f'Sorry, "{self.title}" is currently unavailable.')

    def return_book(self):
        # Return the book and make it available again
        if not self.is_available:
            self.is_available = True
            print(f'You have successfully returned "{self.title}".')
        else:
            print(f'"{self.title}" was not checked out.')

    def get_book_info(self):
        # Return the book information
        availability = "Available" if self.is_available else "Checked out"
        return f'Title: {self.title}, Author: {self.author}, Status: {availability}'

class Library:
    def __init__(self):
        # Initialize the library with an empty catalog
        self.catalog = []

    def add_book(self, book):
        # Add a new book to the library catalog
        self.catalog.append(book)
        print(f'Book "{book.title}" by {book.author} added to the library.')

    def view_catalog(self):
        # View the full list of books in the catalog
        if not self.catalog:
            print("The library catalog is empty.")
        else:
            for book in self.catalog:
                print(book.get_book_info())

def main():
    # Create an instance of Library
    library = Library()

    # Create some books and add them to the library
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", is_available=False)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Display all books in the catalog
    print("\nLibrary Catalog:")
    library.view_catalog()

    # Check out and return books
    print("\nChecking out '1984':")
    book1.check_out()

    print("\nReturning '1984':")
    book1.return_book()

    # Try to check out a book that's not available
    print("\nChecking out 'The Great Gatsby':")
    book3.check_out()

    # View updated catalog after checkout and return
    print("\nUpdated Library Catalog:")
    library.view_catalog()

if __name__ == "__main__":
    main()
