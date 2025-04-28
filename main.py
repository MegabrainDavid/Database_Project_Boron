import tkinter as tk
from tkinter import simpledialog, messagebox
from search import search
from checkout import checkout_book
from checkin import checkin_book
from fines import update_fines, pay_fines
from borrower import add_borrower

def main():
    def search_books():
        query = simpledialog.askstring("Search Books", "Enter search term (ISBN, Title, or Author):")
        if query:
            search(query)

    def checkout():
        update_fines()
        isbn = simpledialog.askstring("Checkout Book", "Enter ISBN to Check Out:")
        card_id = simpledialog.askstring("Checkout Book", "Enter Borrower's Card ID:")
        if isbn and card_id:
            checkout_book(isbn, card_id)

    def checkin():
        isbn = simpledialog.askstring("Checkin Book", "Enter ISBN to Check In (or leave blank):")
        card_id = simpledialog.askstring("Checkin Book", "Enter Borrower's Card ID (or leave blank):")
        name = simpledialog.askstring("Checkin Book", "Enter Borrower Name (or leave blank):")
        checkin_book(isbn, card_id, name)

    def pay_fines_action():
        update_fines()
        pay_fines()

    def add_borrower_action():
        add_borrower()

    # Setup the main window
    root = tk.Tk()
    root.title("📚 Library Management System 📚")
    root.geometry("400x400")

    label = tk.Label(root, text="Choose an action:", font=("Arial", 16))
    label.pack(pady=20)

    # Buttons for each action
    actions = [
        ("🔍 Search Books", search_books),
        ("📖 Checkout Book", checkout),
        ("📥 Checkin Book", checkin),
        ("💵 Pay Fines", pay_fines_action),
        ("➕ Add Borrower", add_borrower_action),
        ("🚪 Exit", root.quit)
    ]

    for (text, command) in actions:
        button = tk.Button(root, text=text, command=command, width=30, height=2)
        button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
