from random import choice

from soupsieve.util import lower

# Lists to store book information
titles = []      # List of book titles
authors = []     # List of book authors
statuses = []    # List of read statuses: "Read" or "Unread"

def add_book(title, author):
    titles.append(title)
    authors.append(author)
    statuses.append('Unread')
    print('This book was successfully added')


def mark_as_read(title):
    flag = False
    for index, book in enumerate(titles):
        if book == title:
            statuses[index] = 'Read'
            flag = True
            break

    if flag:
        print(f'{title} is unred')
    else:
        print('This book is not found')


def mark_as_unread(title):
    flag = False
    for index, book in enumerate(titles):
        if book == title:
            statuses[index] = 'Unread'
            flag = True
            break
    if flag:
        print(f'{title} is unred')
    else:
        print('This book is not found')

def search_book(keyword):
    matches= [(index, title) for index, title in enumerate(titles) if keyword.lower() in title.lower()]

    matches1 = [(index, author) for index, author in enumerate(authors) if keyword.lower() in author.lower()]


    for index, title in matches:
        print(f'{titles[index]} by {authors[index]} is a good book ')

    for index, author in matches1:
        print(f'{titles[index]} by {authors[index]} is a good book ')



    if len(matches) < 1 and len(matches1) < 1:
        print('No books found.')


def list_books():
    for index, value in enumerate(titles):
        print(f' {index} <> {titles[index]} <> {authors[index]}' )


def suggest_book():
    indices = [i for i, x in enumerate(statuses) if x == "Unread"]
    chosen_book = choice(indices)
    if len(indices) >0:
        print(titles[chosen_book])
    else:
        print("No unread books left.")


def delete_book(title):
    for index, value in enumerate(titles):
        if value == title:
            authors.pop(index)
            statuses.pop(index)
    if title in titles:
        titles.remove(title)
        print ("Book was removed.")
    else:
        print("Book not found.")


def main():
    print("📚 Welcome to the Digital Book Collection Manager 📚\n")

    while True:
        print("\nPlease choose an option:")
        print("1. Add a new book")
        print("2. Mark a book as read")
        print("3. Mark a book as unread")
        print("4. Search for a book")
        print("5. List all books")
        print("6. Suggest a book to read")
        print("7. Delete a book")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            add_book(title, author)

        elif choice == '2':
            title = input("Enter the title of the book to mark as read: ")
            mark_as_read(title)

        elif choice == '3':
            title = input("Enter the title of the book to mark as unread: ")
            mark_as_unread(title)

        elif choice == '4':
            keyword = input("Enter a keyword to search: ")
            search_book(keyword)

        elif choice == '5':
            list_books()

        elif choice == '6':
            suggest_book()

        elif choice == '7':
            title = input("Enter the title of the book to delete: ")
            delete_book(title)

        elif choice == '8':
            print("Goodbye! Happy reading! 📖")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 8.")

if __name__ == "__main__":
    main()
