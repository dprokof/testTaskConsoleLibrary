import json
import uuid


class Book:
    def __init__(self, title, author, year, available=True):
        self.book_id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.available = available


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        pass

    def search_book(self, book_id):
        pass

    def display_books(self):
        for book in self.books:
            print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Year: {book.year},"
                  f" Status: {'Available' if book.available else 'Not available'}")

    def lend_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and book.available:
                book.available = False
                print(f"{book.title} has been lent out.")
                self.save_to_json()
                return
        print("Book not available for lending.")

    def load_from_json(self):
        try:
            with open('books.json', 'r') as file:
                data = json.load(file)
                for item in data:
                    book = Book(item['title'], item['author'], item['year'], item['available'])
                    book.book_id = item['book_id']
                    self.books.append(book)
        except FileNotFoundError:
            self.books = []

    def save_to_json(self):
        data = []
        for book in self.books:
            data.append({'book_id': book.book_id, 'title': book.title,
                         'author': book.author, 'available': book.available})

        with open('books.json', 'w') as file:
            json.dump(data, file, indent=4)


if __name__ == '__main__':
    print('Welcome to Library Managment System!')
    print('1 - Add book\n'
          '2 - Delete book\n'
          '3 - Search book\n'
          '4 - Display books\n'
          '5 - Lend book\n')
    command = int(input('Please, enter number of command: '))