from random import choice
from datetime import datetime


class Book:

    on_shelf = []
    on_loan = []

    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    @classmethod
    def create(cls, author, title, ISBN):
        new_book = Book( author, title, ISBN)
        cls.on_shelf.append(new_book)
        return new_book

    @classmethod
    def browse(cls):
        book = choice(cls.on_shelf)
        return book

    def lent_out(self):
        return self in Book.on_loan

    @classmethod
    def current_due_date(cls):
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14   # two weeks expressed in seconds
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp)

    def borrow(self):
        if self.lent_out():
            return False
        else:
            self.due_date = Book.current_due_date()
            Book.on_shelf.remove(self)
            Book.on_loan.append(self)
            return True

    def return_to_library(self):
        if not self.lent_out():
            return False
        else:
            Book.on_loan.remove(self)
            Book.on_shelf.append(self)
            self.due_date = None
            return True

    @classmethod
    def overdue(cls):
        overdue_books = []
        for num in range(0, len(Book.on_loan)):
            current_book = Book.on_loan[num]
            if current_book.due_date < datetime.now():
                overdue_books.append(current_book)
            return overdue_books
