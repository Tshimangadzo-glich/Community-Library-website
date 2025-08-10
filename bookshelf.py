# bookshelf.py

bookshelf = []

def add_book(title, author):
    bookshelf.append({'title': title, 'author': author})
    print(f"Added: '{title}' by {author}")

def list_books():
    if not bookshelf:
        print("Your bookshelf is empty.")
    else:
        print("Books on your shelf:")
        for i, book in enumerate(bookshelf, 1):
            print(f"{i}. {book['title']} by {book['author']}")

def remove_book(index):
    try:
        removed = bookshelf.pop(index - 1)
        print(f"Removed: '{removed['title']}' by {removed['author']}")
    except IndexError:
        print("Invalid index. No book removed.")

# Example usage
add_book("The Hobbit", "J.R.R. Tolkien")
add_book("1984", "George Orwell")
add_book("To Kill a Mockingbird", "Harper Lee")
add_book("Pride and Prejudice", "Jane Austen")
add_book("The Great Gatsby", "F. Scott Fitzgerald")
add_book("The Catcher in the Rye", "J.D. Salinger")
add_book("The Alchemist", "Paulo Coelho")
add_book("The Da Vinci Code", "Dan Brown")
add_book("The Lord of the Rings", "J.R.R. Tolkien")
list_books()
remove_book(1)
list_books()