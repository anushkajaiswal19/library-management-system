from utils import books
def addbook():
    print("Adding a book...")
    bookname=input("Enter the name of the book: ").upper()
    books.append(bookname)
    print(bookname," has been added to the library.")