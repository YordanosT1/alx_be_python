#Task 1: 1. Mastering Inheritance and Composition in Python
'''
Develop two Python scripts: library_system.py and main.py. In library_system.py, 
you’ll define a base class Book and two derived classes, EBook and PrintBook, 
showcasing inheritance. Additionally, implement a Library class demonstrating composition 
by managing a collection of books.
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

#classes that inherit from the class Book
class EBook(Book):
    def __init__(self, file_size):
        self.file_size = file_size
    def __int__(self):
        return f"{self.file_size}"
 #Set up the class library
class PrintBook(Book):
    def __init__(self, page_count):
        self.page_count = page_count
    def __int__(self):
        return f"{self.page_count}"
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)  