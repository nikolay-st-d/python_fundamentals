book_to_search = input()

books_number = 0

while True:
    book = input()
    books_number += 1

    if book == 'No More Books':
        print(f'The book you search is not here!')
        print(f'You checked {books_number - 1} books.')
        break

    elif book == book_to_search:
        print(f'You checked {books_number - 1} books and found it.')
        break
