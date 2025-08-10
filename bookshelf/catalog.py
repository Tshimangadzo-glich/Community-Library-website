# Library Bookshelf Catalog Management
catalog = []

def add_book(title, author, genre):
    catalog.append({'title': title, 'author': author, 'genre': genre})
    print(f"Added: '{title}' by {author} [{genre}]")

def list_books():
    if not catalog:
        print("The catalog is empty.")
    else:
        print("Library Catalog:")
        for i, book in enumerate(catalog, 1):
            print(f"{i}. {book['title']} by {book['author']} ({book['genre']})")

def search_by_genre(genre):
    results = [book for book in catalog if book['genre'].lower() == genre.lower()]
    if results:
        print(f"Books in genre '{genre}':")
        for book in results:
            print(f"- {book['title']} by {book['author']}")
    else:
        print(f"No books found in genre '{genre}'.")

add_book("The Hobbit", "J.R.R. Tolkien", "Fantasy")
add_book("harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy")
add_book("Educated", "Tara Westover", "Non-Fiction")
add_book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
add_book("The Catcher in the Rye", "J.D. Salinger", "Classic")
add_book("The Alchemist", "Paulo Coelho", "Adventure")
list_books()
search_by_genre("Fantasy")