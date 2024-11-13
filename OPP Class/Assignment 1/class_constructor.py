#creating a book with special attributes
class Book:
    #constructor method to initialize book attributes
    def __init__(self, title, author, publication_year, genre, isbn):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.isbn = isbn

        #initialize book status as available
        self.available = True
   
    #method to check if book is available for borrowing
    def is_available(self):
        return self.available
    
    #method to borrow book by updating availability status
    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"You have successfully borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' is currently not available for borrowing.")
#Adding an inheritance layer to explore polymorphism or encapsulation
class EBook(Book):
    def __init__(self, title, author, publication_year, genre, isbn, file_format, file_size):
        super().__init__(title, author, publication_year, genre, isbn)
        self.file_format = file_format
        self.file_size = file_size

    def download_ebook(self):
        print(f"You have downloaded '{self.title}' by {self.author} in {self.file_format} format.")

    def view_ebook(self):
        print(f"You have viewed '{self.title}' by {self.author} in {self.file_format} format.")

#Creating 3 objects with instances of EBook and Book object
ebook1 = EBook("Python Programming", "John Doe", 2022, "Technology", "1234567890", "PDF", "20MB")
ebook2 = EBook("C++ Programming", "Jane Smith", 2021, "Technology", "9876543210", "EPUB", "15MB")
book3 = Book("English Grammar", "Mary Johnson", 2019, "Reference", "0123456789")

#Testing the is_available method of EBook and Book objects
print(ebook1.is_available())
print(book3.is_available())

#Testing the methods of EBook and Book objects
ebook1.download_ebook()
ebook1.view_ebook()

ebook2.download_ebook()
ebook2.view_ebook()
