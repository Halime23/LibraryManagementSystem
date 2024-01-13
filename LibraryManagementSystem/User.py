class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.borrowed_books = []

    def display_info(self):
        print(f"Name: {self.name}\nEmail: {self.email}")

    def display_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s borrowed books:")
            for book in self.borrowed_books:
                print(f"{book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")

