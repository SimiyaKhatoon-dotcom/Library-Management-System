import datetime
import time
user=[]
library=[]
def register_user():
    username=input("enter name of user: ")
    user.append(username)
    print(f"{username} has been registered")
def user_login():
    username=input("enter name of user: ")
    if username in user:
        print("Login successful")
    else:
        print("User not found")
def add_books():
    book=input("Enter book name: ")
    library.append(book)
    print(f"'{book}' has been added")
def issue_books():
    book=input("Enter book to be issued: ")
    if book in library:
        library.remove(book)
        print(f"'{book}'has been issued")
    else:
        print("Book not found")
def return_books():
    book=input("Enter book to be returned: ")
    library.append(book)
    return_date=datetime.datetime.now()
    print(f"'{book}' has been returned on date : {return_date}")
def track_duedate():
    for book in library:
        book=input("enter book to track due date:")
        due_date=datetime.datetime.now()+datetime.timedelta(days=21)
        print("Due date: ",due_date.date())
        break
def over_due():
    for days in library:
        days=int(input("Enter no of days: "))
        if days>21:
            print("Fine of Rs.",5*(days-21))
            break
def view_books():
    if not library:
        print("Library is empty")
    else:
        print("List of books")
        idx=1
        for book in library:
            print(f"{idx}. {book}")
            idx+=1
        print("")
while True:
    print("-----LIBRARY MANAGEMENT SYSTEM-----")
    print("1. Register user")
    print("2. User login")
    print("3. Add book")
    print("4. Isuue book")
    print("5. Return book")
    print("6. Track due date")
    print("7. Overdue")
    print("8. View books")
    print("9. Exit")

    choice =int(input("Enter your choice: "))
    if choice==1:
        register_user()
    elif choice==2:
        user_login()
    elif choice==3:
        add_books()
    elif choice==4:
        issue_books()
    elif choice==5:
        return_books()
    elif choice==6:
        track_duedate()
    elif choice==7:
        over_due()
    elif choice==8:
        view_books()
    elif choice==9:
        print("THANK YOU , You are now exiting the library management system")
        break
    else:
        print("Invalid choice. Try again")
    time.sleep(1)