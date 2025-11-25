import os
import json
from book import Book
from member import Member

# ------------------------------------
#   Library CLASS
# ------------------------------------

class Library:
    def __init__(self, books_file="books.json", members_file="members.json"):
        self.books_file = books_file
        self.members_file = members_file

        # Load existing data
        self.books = self._read_file(self.books_file)
        self.members = self._read_file(self.members_file)

    # ------------ File Handling --------------
    def _read_file(self, path):
        if not os.path.exists(path):
            return {}
        with open(path, "r") as f:
            return json.load(f)

    def _save_file(self, path, data):
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    # ------------ Library Operations --------------
    def add_book(self, book: Book):
        self.books[book.book_id] = book.to_dict()
        self._save_file(self.books_file, self.books)
        print("\n✔ Book added successfully!")

    def add_member(self, member: Member):
        self.members[member.member_id] = member.to_dict()
        self._save_file(self.members_file, self.members)
        print("\n✔ Member added successfully!")

    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("\n❌ Member ID not found.")
            return
        
        if book_id not in self.books:
            print("\n❌ Book ID not found.")
            return

        if not self.books[book_id]["available"]:
            print("\n❌ Book already borrowed.")
            return

        self.books[book_id]["available"] = False
        self.members[member_id]["borrowed_books"].append(book_id)

        self._save_file(self.books_file, self.books)
        self._save_file(self.members_file, self.members)
        print("\n📘 Book borrowed successfully!")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("\n❌ Member ID invalid.")
            return
        
        if book_id not in self.members[member_id]["borrowed_books"]:
            print("\n❌ This member did not borrow this book.")
            return

        self.members[member_id]["borrowed_books"].remove(book_id)
        self.books[book_id]["available"] = True

        self._save_file(self.books_file, self.books)
        self._save_file(self.members_file, self.members)
        print("\n🔄 Book returned successfully!")

    def show_books(self):
        print("\n------ Library Books ------")
        if not self.books:
            print("No books available.")
            return

        for b in self.books.values():
            status = "Available" if b["available"] else "Borrowed"
            print(f'{b["book_id"]} | {b["title"]} | {b["author"]} | {status}')

    def show_members(self):
        print("\n------ Members List ------")
        if not self.members:
            print("No members registered.")
            return

        for m in self.members.values():
            print(f'{m["member_id"]} | {m["name"]} | Borrowed: {m["borrowed_books"]}')
