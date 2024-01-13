from tkinter import messagebox
from library_db import LibraryDB


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.borrowed_books = {}
        self.library_db = LibraryDB()

    def add_book(self, book):
        self.library_db.add_book(book)
        self.books.append(book)

    def remove_book(self, title):
        book = self.search_book(title, return_book=True)
        if book:
            try:
                print(f"Removing book from library: {book}")
                self.books.remove(book)
                self.library_db.remove_book(book)
                print(f"{book['title']} removed from the library.")
                return True  # Kitap bulundu ve silindi
            except Exception as e:
                print(f"Error while removing book: {e}")
                return False  # Kitap silinirken hata oluştu
        else:
            print(f"{title} not found in the library.")
            return False  # Kitap bulunamadı

    def list_books(self):
        print("Books in the library:")
        for book in self.books:
            book_info = f"{book.title} by {book.author} ({book.category})"
            if book.is_borrowed:
                book_info += f" (Borrowed by: {book.borrower})"
                if book.due_date:
                    book_info += f", Due Date: {book.due_date}"

    def get_book_by_isbn(self, isbn):
        for book in self.books:
            if book.ISBN == isbn:
                return book
        return None

    def update_book(self, updated_book):
        pass

    def get_book_info(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return {
                    'title': book.title,
                    'author': book.author,
                    'ISBN': book.isbn,
                    'category': book.category,
                    'is_borrowed': book.is_borrowed,
                    'borrower': book.borrower,
                }
        return None

    def search_book(self, title, return_book=False):
        for book in self.books:
            if book.title == title:
                if return_book:
                    return book
                else:
                    book.display_info()
                    return
        print(f"{title} not found in the library.")
        if return_book:
            return None

    def add_user(self, user):
        self.library_db.add_user(user)
        self.users.append(user)
        messagebox.showinfo("Success", f"User {user.name} added to the library.")

