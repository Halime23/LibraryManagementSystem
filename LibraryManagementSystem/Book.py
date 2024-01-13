class Book:
    def __init__(self, title, author, ISBN, category, is_borrowed, borrower_name):
        self.id = None
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.category = category
        self.is_borrowed = is_borrowed
        self.borrower = borrower_name

    def get_title(self):
        return self.title

    def set_title(self, new_title):
        self.title = new_title

    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.ISBN}\nCategory: {self.category}")
        if self.is_borrowed:
            print(f"Borrowed by: {self.borrower}")
