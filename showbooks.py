from utils import books
def showbooks():
    if len(books)==0:
        print("No books in the library.")
    else:
        for i in books:
            print(i)