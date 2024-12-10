import sqlite3

def add_book(cusros):
    pass

def borrow_book(cusros):
    pass

def return_book(cusros):
    pass

def view_available_books(cusros):
    pass

if __name__ == "__main__":

    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS book(title TEXT, author TEXT, available BINARY)")


    while True:
        menu = int(input('''WELCOME TO OUR LIBRARY! How can I help you?\n
        1) View Available Books\n
        2) Borrow Book\n
        3) Return Book\n
        4) Add Book to our library\n
        5) Exit\n
            '''))
        if menu == 1:
            view_available_books(cursor)
        elif menu == 2:
            borrow_book(cursor)
        elif menu == 3:
            return_book(cursor)
        elif menu == 4:
            add_book(cursor)
        else:
            print("See you later!")
            break
        
    connection.close()