from config import get_db_connection

# Establish database connection
conn = get_db_connection()
cursor = conn.cursor()

# Function to Add a Book
def add_book():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    isbn = input("Enter ISBN: ")

    try:
        cursor.execute("INSERT INTO books (title, author, isbn) VALUES (%s, %s, %s)", 
                       (title, author, isbn))
        conn.commit()
        print("✅ Book added successfully!")
    except Exception as e:
        print("❌ Error:", e)

# Function to View All Books
def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    if not books:
        print("📌 No books found in the library!")
    else:
        print("\n📚 Library Books:")
        for book in books:
            print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | ISBN: {book[3]}")

# Function to Update a Book
def update_book():
    book_id = input("Enter Book ID to Update: ")
    title = input("Enter New Title: ")
    author = input("Enter New Author: ")
    isbn = input("Enter New ISBN: ")

    try:
        cursor.execute("UPDATE books SET title=%s, author=%s, isbn=%s WHERE id=%s", 
                       (title, author, isbn, book_id))
        conn.commit()
        print("✅ Book updated successfully!")
    except Exception as e:
        print("❌ Error:", e)

# Function to Delete a Book
def delete_book():
    book_id = input("Enter Book ID to Delete: ")

    try:
        cursor.execute("DELETE FROM books WHERE id=%s", (book_id,))
        conn.commit()
        print("✅ Book deleted successfully!")
    except Exception as e:
        print("❌ Error:", e)

# Main Menu
while True:
    print("\n📚 Library Management System")
    print("1️⃣ Add Book")
    print("2️⃣ View Books")
    print("3️⃣ Update Book")
    print("4️⃣ Delete Book")
    print("5️⃣ Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        update_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        print("👋 Exiting...")
        break
    else:
        print("❌ Invalid choice. Please try again.")

# Close database connection
cursor.close()
conn.close()
