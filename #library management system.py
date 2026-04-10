books = [
    ["101", "Harry Potter and the Sorcerer's Stone", 2],
    ["102", "The Hobbit", 1],
    ["103", "The Lion, the Witch and the Wardrobe", 1]
]

while True:
    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    # Add Book
    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")

        found = False
        for b in books:
            if b[0] == book_id:
                b[2] += 1
                found = True
                print(f"{b[1]} → Copies now: {b[2]}")
                break

        if not found:
            books.append([book_id, title, 1])
            print(f"{title} added → Copies now: 1")

    # Show Books
    elif choice == "2":
        if not books:
            print("No books available")
        else:
            print("\n--- Book List ---")
            for b in books:
                if b[2] > 0:
                    print(f"{b[0]} - {b[1]} - Copies: {b[2]}")
                else:
                    print(f"{b[0]} - {b[1]} - Not Available")

    # Issue Book
    elif choice == "3":
        book_id = input("Enter Book ID: ")
        found = False

        for b in books:
            if b[0] == book_id:
                found = True
                if b[2] > 0:
                    b[2] -= 1
                    print(f"{b[1]} issued → Copies left: {b[2]}")
                else:
                    print(f"{b[1]} is not available!")
                break

        if not found:
            print("Book not found!")

    # Return Book
    elif choice == "4":
        book_id = input("Enter Book ID: ")
        found = False

        for b in books:
            if b[0] == book_id:
                b[2] += 1
                found = True
                print(f"{b[1]} returned → Copies now: {b[2]}")
                break

        if not found:
            print("Book not found!")

    # Exit
    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")