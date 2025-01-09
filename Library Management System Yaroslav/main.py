import sqlite3

def add_book(cursor):
    title = input("Please, insert title:\n")
    author = input("And author:\n")
    cursor.execute(f"INSERT INTO book (title, author, available) VALUES ('{title}', '{author}', True)")

def borrow_book(cursor):
    pk = input("Please, insert id:\n")
    cursor.execute(f"UPDATE book SET available = False WHERE pk = '{pk}'")

def return_book(cursor):
    pk = input("Please, insert id:\n")
    cursor.execute(f"UPDATE book SET available = True WHERE pk = '{pk}'")

def view_available_books(cursor):
    cursor.execute('''SELECT * FROM book WHERE available''')
    output = cursor.fetchall()
    return output

if __name__ == "__main__":

    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS book(pk INTEGER NOT NULL PRIMARY KEY, title TEXT, author TEXT, available BINARY)")


    while True:
        menu = int(input('''WELCOME TO OUR LIBRARY! How can I help you?\n
        1) View Available Books\n
        2) Borrow Book\n
        3) Return Book\n
        4) Add Book to our library\n
        5) Exit\n
            '''))
        if menu == 1:
            for row in view_available_books(cursor):
                print(row)
        elif menu == 2:
            borrow_book(cursor)
        elif menu == 3:
            return_book(cursor)
        elif menu == 4:
            add_book(cursor)
        else:
            print("See you later!")
            connection.commit()
            break
        
    connection.close()