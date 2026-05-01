from utils import books, issued_book
def issuebook():
    bookname=input("Enter the name of the book to issue: ").upper()
    if bookname in books:
        books.remove(bookname)
        issued_book.append(bookname)
        print(bookname, "has been issued.")
    else:
        print(bookname," is not available in the library.")