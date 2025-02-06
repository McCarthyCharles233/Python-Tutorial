library = []

while True:
    action = input("Enter action(add, view, borrow, return, exit): ").strip().lower()
    if action == 'add':
        title = input("Enter the title of the book: ").strip().lower()
        author = input("Enter the Author of the book: ").strip().lower()

        book = {
            "title": title,
            "author": author,
            "borrowed": False
        }
        library.append(book)

        print("Book added successfully!")

    elif action == "view":
        if len(library) == 0:
            print("no books available")
        else:
            print("\nLibrary Collection:")
            for book in library:
                status = "Borrowed" if book["borrowed"] else "Available"
                print(f"Title: {book['title'].title()}, Author: {book['author'].title()}, Status: {status}")
            print()

    elif action == "borrow":
        title = input("What is the title of the book: ").strip().lower()
        found = False

        for book in library:
            if book["title"] == title:
                found = True
                if book["borrowed"]:
                    print("This book is already borrowed.\n")
                else:
                    book["borrowed"] = True
                    print(f'You have borrowed "{book["title"].title()}". Enjoy reading!\n')
                break

        if not found:
            print("Book not found.\n")


    elif action == "return":
        title = input("Enter the title of the book you want to return: ").strip().lower()
        found = False

        for book in library:
            if book["title"] == title:
                found = True
                if not book["borrowed"]:
                    print("This book was not borrowed.\n")
                else:
                    book["borrowed"] = False
                    print(f'You have returned "{book["title"].title()}". Thank you!\n')
                break

        if not found:
            print("Book not found.\n")


    elif action == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid action, try again.")
