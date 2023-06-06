class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Available: {self.is_available}"


class LibraryMember:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed the book '{book.title}' by {book.author}.")
        else:
            print(f"The book '{book.title}' by {book.author} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned the book '{book.title}' by {book.author}.")
        else:
            print(f"The book '{book.title}' by {book.author} is not borrowed by {self.name}.")

    def display_borrowed_books(self):
        print(f"Borrowed Books by {self.name}:")
        for book in self.borrowed_books:
            print(book)


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print(f"Books available in {self.name}:")
        for book in self.books:
            print(book)


def main():
    # Membuat objek LibraryMember
    member = LibraryMember(input("Enter member name: "))

    # Membuat objek Library
    library = Library("My Library")

    # Membuat objek Book
    book1 = Book("Judul Buku", "seno")
    book2 = Book("Judul Buku 101", "Nohan")
    book3 = Book("Judul Buku", "Rifki")

    # Menambahkan buku ke perpustakaan
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Meminjam buku
    borrow_option = input("Apakah Kamu Mau Minjam Buku? (Y/N): ")
    while borrow_option.upper() == "Y":
        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")
        book = Book(book_title, book_author)
        member.borrow_book(book)
        borrow_option = input("Apakah Kamu Mau MInjam Buku Lain ? (Y/N): ")

    # Mengembalikan buku
    return_option = input("Apakah Kamu Mau Mengembalikan Buku? (Y/N): ")
    while return_option.upper() == "Y":
        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")
        book = Book(book_title, book_author)
        member.return_book(book)
        return_option = input("Apakah Kamu Mau MInjam Buku Lain? (Y/N): ")

    # Menampilkan daftar buku yang dipinjam
    display_option = input("Apakah Kamu Mau Melihat Buku Yang Di pinjam? (Y/N): ")
    if display_option.upper() == "Y":
        member.display_borrowed_books()

    # Menampilkan daftar buku yang tersedia di perpustakaan
    list_option = input("Apakah Kamu Mau MIlihat Daftar Buku? (Y/N): ")
    if list_option.upper() == "Y":
        library.display_books()


if __name__ == "__main__":
    main()
