import unittest
from library_management import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.books = [
            {"id": 1, "title": "1984", "author": "George Orwell", "available": True},
            {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "available": True},
            {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "available": False},
        ]
        self.library = Library(books_list=self.books)

    def test_add_books(self):
        self.library.add_books(4, "Brave New World", "Aldous Huxley")
        self.assertEqual(len(self.library.books), 4)
        self.assertEqual(self.library.books[-1]["title"], "Brave New World")

    def test_add_duplicate_books(self):
        self.library.add_books(1, "Duplicate Book", "Author Name")
        self.assertEqual(len(self.library.books), 3)  

    def test_borrow_books(self):
        self.library.borrow_books(1)
        self.assertFalse(self.library.books[0]["available"])

    def test_borrow_unavailable_book(self):
        self.library.borrow_books(3)
        self.assertFalse(self.library.books[2]["available"]) 

    def test_return_books(self):
        self.library.return_book(3)
        self.assertTrue(self.library.books[2]["available"])

    def test_return_available_book(self):
        self.library.return_book(1)
        self.assertTrue(self.library.books[0]["available"]) 

    def test_view_available_books(self):
        self.library.view_available_books()
        available_books = [book for book in self.books if book["available"]]
        self.assertEqual(len(available_books), 2)

if __name__ == "__main__":
    unittest.main()
