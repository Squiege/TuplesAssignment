# Task 1

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def new_book(library):
    book_title = input("What is the title of the book you would like to add?")
    book_author = input("What is the author's name of the book you would like to add?")
    for book in library:
        if book[0] != book_title:
            book_tuple = (book_title, book_author)
            library.append(book_tuple)
            print(library)
            return
        else:
            print("Book already in library!")


new_book(library)