from library import Library
from book import Book
from member import Member

# ------------------------------------
#       MAIN PROGRAM
# ------------------------------------

def main():
    lib = Library()

    while True:
        print("\n========== Library Menu ==========")
        print("1. Add a New Book")
        print("2. Register a Member")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. View All Books")
        print("6. View All Members")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Book Title: ")
            author = input("Author Name: ")
            lib.add_book(Book(book_id, title, author))

        elif choice == "2":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            lib.add_member(Member(member_id, name))

        elif choice == "3":
            member_id = input("Enter Member ID: ")
            book_id = input("Enter Book ID: ")
            lib.borrow_book(member_id, book_id)

        elif choice == "4":
            member_id = input("Enter Member ID: ")
            book_id = input("Enter Book ID: ")
            lib.return_book(member_id, book_id)

        elif choice == "5":
            lib.show_books()

        elif choice == "6":
            lib.show_members()

        elif choice == "7":
            print("\nGoodbye! 👋")
            break

        else:
            print("\n❌ Invalid option. Try again.")


if __name__ == "__main__":
    main()
