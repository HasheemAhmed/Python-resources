# library Management System

LibraryBooks = list()

Authors = set()

BooksCount = {}

def add_book(title,author,year):
    book = (title,author,year)
    LibraryBooks.append(book)
    Authors.add(author)

    if book in BooksCount:
        BooksCount[book] += 1
    else:
        BooksCount[book] = 1

    print(f"{title} by {author} is added to library")

def remove_book(title,author,year):
    book = (title,author,year)
    
    if book in BooksCount:
        BooksCount[book] -= 1
        LibraryBooks.remove(book)
        
        if BooksCount[book] == 0:
            Authors.remove(author)
            BooksCount.pop(book)

    print(f"{title} by {author} is remove from library")

def search_book(title ):
    
    sort = True
    for x in LibraryBooks:
        if x[0].lower() == title.lower():
            print(f"{title} by {x[1]} in {x[2]} is in the library.")
            sort = False
    
    if sort:
        print(f"{title} is not in the library.")

def list_books():
    if LibraryBooks:
        for x in LibraryBooks:
            print(f'{x[0].capitalize()} by {x[1].capitalize()} in {x[2]}')
    else:
        print('No books in the library.')


def list_Authors():
    if Authors:
        for x in Authors:
            print(x)
    else:
        print('No Authors.')

def search_book_by_author(author):
    
    sort = True
    for x in LibraryBooks:
        if x[1].lower() == author.lower():
            print(f"{x[0]} by {x[1]} in {x[2]} is in the library.")
            sort = False
    
    if sort:
        print(f"No books by {author} is not in the library.")


def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book by title")
        print("4. List all books")
        print("5. List all authors")
        print("6. Find books by a specific author")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter publication year: ")
            add_book(title, author, year)
        elif choice == '2':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter publication year: ")
            remove_book(title, author, year)
        elif choice == '3':
            title = input("Enter book title: ")
            search_book(title)
        elif choice == '4':
            list_books()
        elif choice == '5':
            list_Authors()
        elif choice == '6':
            author = input("Enter book author: ")
            search_book_by_author(author)
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()