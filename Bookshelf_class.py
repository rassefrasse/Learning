class Book:
    def __init__(self, title, author, year, genre): #This is for the books
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre


class Bookshelf:
    def __init__(self):
        self.bookshelf_horror = [] #Three different bookshelves depending on genre
        self.bookshelf_fantasy = []
        self.bookshelf_romance = []

    def bookshelf_storage(self, author, year, title, genre): 
        book_instance = Book(title, author, year, genre)
        if genre == 'horror':
            self.bookshelf_horror.append(book_instance)
        elif genre == 'fantasy':
            self.bookshelf_fantasy.append(book_instance)
        elif genre == 'romance':
            self.bookshelf_romance.append(book_instance)
        else:
            print("not a valid genre")

bookshelf_instance = Bookshelf()

author = input("What's the name of the author: ").lower()
year = input("What's the release year of the book:  ").lower()
title = input("What's the name of the book: ").lower()
genre = input("What's the genre of the book: ").lower()

bookshelf_instance.bookshelf_storage(author, year, title, genre)

horror = bookshelf_instance.bookshelf_horror
fantasy = bookshelf_instance.bookshelf_fantasy
romance = bookshelf_instance.bookshelf_romance

print("Horror: ")
for book in horror:
    print(f"Author: {book.author} Genre: {book.genre} Title: {book.title} Release: {book.year}")

print("Fantasy: ")
for book in fantasy:
    print(f"Author: {book.author} Genre: {book.genre} Title: {book.title} Release: {book.year}")

print("Romance: ")
for book in romance:
    print(f"Author: {book.author} Genre: {book.genre} Title: {book.title} Release: {book.year}")
