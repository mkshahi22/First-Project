import random

# Welcome message and user registration
print("Hii! Welcome to Our Library\nPlease give your name below for record!")
username = input("Enter Your Name: ")
userid = random.randint(10000, 99999)
books = ["Python", "HTML", "CSS", "Java", "AI"]
print("Thank you", username, "Your ID Number is", userid)

while True:
    # Menu options
    print("\nChoose a number from this list:")
    print("1. Search a Book")
    print("2. Allot me a Book")
    print("3. Return Book")
    print("4. Exit Library")
    
    # User choice input
    userch = int(input("Enter the number 1 to 4: "))
    
    # Handling user choices
    if userch == 1:
        # Search for a book
        search = input("Search Book Name: ")
        if search in books:
            print(search, "Book is Available")
        else:
            print(search, "Book is not available")
        print("Available Books are", books)
    
    elif userch == 2:
        # Allot a book
        bookname = input("Enter Book Name for Allotting: ")
        if bookname in books:
            print(bookname, "is Allotted")
            books.remove(bookname)
        else:
            print(bookname, "is not available")
        print("Available Books are", books)
    
    elif userch == 3:
        # Return a book
        returnbook = input("Enter Book Name for Returning: ")
        books.append(returnbook)
        print("Thank you for returning the book", username)
        print("Available Books are now", books)
    
    elif userch == 4:
        # Exit the library
        print("Ok, Good Bye...!")
        break
    
    else:
        # Invalid choice
        print("Invalid Choice")
