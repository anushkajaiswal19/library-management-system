from addbooks import addbook
from showbooks import showbooks
from issuebook import issuebook
from returnbook import returnbook

def library():
    while True:
        print('\n1. Add Book')
        print('\n2. Show Books') 
        print('\n3. Issue Book')
        print('\n4. Return Book')
        print('\n5. Exit')

        choice=int(input('\nEnter your choice: '))
        
        if choice==1: 
            addbook()
        elif choice==2:
            showbooks()
        elif choice==3:
            issuebook()
        elif choice==4:
            returnbook()
        elif choice==5:
            print("Thank You")
            break
        else:
            print("Invalid Choice")
library()