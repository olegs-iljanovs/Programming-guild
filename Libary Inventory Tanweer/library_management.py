class Library:
    def __init__(self, books_list=None):
        self.books = books_list if books_list else []

    def add_book(self, book_id, book_title, author_name):
        for book in self.books:
            if book.get("id") == book_id:
                print("Book with ID {} already exists.".format(book_id))
                return
        self.books.append({"id": book_id, "title": book_title, "author": author_name, "available": True})
        print("Book '{}' by {} added successfully!".format(book_title, author_name, book_id))


    def borrow_book(self, book_id):
        for book in self.books:
            if book.get("id") == book_id:
                if book.get("available"):
                    book["available"] = False
                    print("You have borrowed '{}' by {}.".format(book["title"], book["author"]))
                else:
                    print("Sorry, '{}' is currently unavailable.".format(book["title"]))
                return

        print("Book with ID {} does not exist.".format(book_id))

    def return_book(self, book_id):
        book = next((b for b in self.books if b.get("id") == book_id), None)
        if not book:
            print(f"Book with ID {book_id} does not exist.")
            return False
        if book["available"]:
            print(f"'{book['title']}' is already available in the library.")
            return False
        book["available"] = True
        print(f"Thank you for returning '{book['title']}' by {book['author']}.")
        return True


    def view_available_books(self):
        available_books = [book for book in self.books if book.get("available")]
        if not available_books:
            print("No books are currently available.")
            return
        print("Available Books:")
        print("{:<10}{:<30}{:<20}".format("ID", "Title", "Author"))
        print("-" * 60)
        for book in available_books:
            print("{:<10}{:<30}{:<20}".format(book["id"], book["title"], book["author"]))
        print("-" * 60)


books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "available": True},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "available": True},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "available": False},
]

library = Library(books_list=books)

# add books
library.add_book(4, "Brave New World", "Aldous Huxley")
library.add_book(1, "Duplicate Book", "Author Name")  # duplicate ID

# borrow books
library.borrow_book(1)
library.borrow_book(3)  # already borrowed
library.borrow_book(5)  # invalid ID

# return books
library.return_book(1)
library.return_book(3)
library.return_book(5)  # invalid ID

# view available books
library.view_available_books()
