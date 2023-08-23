class Book:

    def __init__(self, author, title, release, genre): #Initializing 
        self.author = author
        self.title = title
        self.release = release
        self.genre = genre

    def __str__(self): #the string response from the loop
        return f"Author: {self.author}, Title: {self.title}, Release: {self.release}, Genre: {self.genre}"


class Library:

    bookshelf1 = []
        
    @classmethod
    def bookshelf_sorting(cls, book):
        cls.bookshelf1.append(book)

    @classmethod
    def print_bookshelf(cls):
         for book in cls.bookshelf1:
              print(book)



book1 = Book("Tolkien", "Lord of the Rings", 1954, "Fantasy")
book2 = Book("George R.R. Martin", "A Song of Ice and Fire", "unknown", "Fantasy")

Library.bookshelf_sorting(book1)
Library.bookshelf_sorting(book2)

Library.print_bookshelf()

    


