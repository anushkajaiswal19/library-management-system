from utils import books, issued_book
def  returnbook():
    bookname=input("Enter the name of the book to return: ").upper()
    if bookname in issued_book:
        issued_book.remove(bookname)
        books.append(bookname)
        print(f"'{bookname}' has been returned.")
    else:
        print(f"'{bookname}' was not issued from the library.")