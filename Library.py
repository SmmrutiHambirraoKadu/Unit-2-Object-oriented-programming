class Library:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.available = True

    def checkout(self):
        if self.available:
            self.available = False
            print(self.book_name, "checked out")
        else:
            print(self.book_name, "is not available")

    def return_book(self):
        self.available = True
        print(self.book_name, "returned")

    def display(self):
        status = "Available" if self.available else "Not Available"
        print(self.book_name, "-", self.author, "-", status)


# Driver Code
b1 = Library("Python Basics", "Guido")
b1.display()
b1.checkout()
b1.display()
b1.return_book()
b1.display()
