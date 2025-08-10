# fantasy.py

fantasy_books = []

def add_fantasy_book(title, author, magic_level):
    fantasy_books.append({
        'title': title,
        'author': author,
        'magic_level': magic_level
    })
    print(f"Added: '{title}' by {author} [Magic Level: {magic_level}]")

def list_fantasy_books():
    if not fantasy_books:
        print("No fantasy books in the catalog.")
    else:
        print("Fantasy Book Catalog:")
        for i, book in enumerate(fantasy_books, 1):
            print(f"{i}. {book['title']} by {book['author']} (Magic Level: {book['magic_level']})")

def search_by_magic_level(level):
    results = [book for book in fantasy_books if book['magic_level'] == level]
    if results:
        print(f"Books with Magic Level {level}:")
        for book in results:
            print(f"- {book['title']} by {book['author']}")
    else:
        print(f"No books found with Magic Level {level}.")

# Example usage
add_fantasy_book("Mistborn", "Brandon Sanderson", "High")
add_fantasy_book("The Name of the Wind", "Patrick Rothfuss", "Medium")
list_fantasy_books()
search_by_magic_level("High")