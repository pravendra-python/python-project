books = []

while True:
    print("\n=====Library Management System=====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        title = input("Enter Book Title:")
        author = input("Enter Author Name:")

        book = {
            "title": title,
            "author": author
        }

        books.append(book)
        print("Book Added Successfully!")

    elif choice == "2":
        print("\nBook List:")

        for book in books:
            print("Title:",book["title"])
            print("Author:",book["author"])
            print("----------------")


    elif choice =="3":
        search_title = input("Enter Book Title to Search: ")

        found = False

        for book in books:
            if book["title"] ==search_title:
                print("Book Found!")
                print("Title :",book["title"])
                print("Author:",book["author"])
                found = True
                break
        if not found:
            print("Book Not Found!")


    elif choice == "4":
        delete_title = input(" Enter Book Title to Delete: ")
        
        found = False

        for book in books:
            if book["title"] == delete_title:
                books.remove(book)
                print("Book Deleted Successfully!")
                found = True
                break
        if not found:
            print("Book Not Found!")
