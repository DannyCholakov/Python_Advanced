def classify_books(*args, **kwargs):
    fiction_books = []
    non_fiction_books = []
    served_fiction_books = []
    served_non_fiction_books = []

    # Process the tuples first
    for genre, title in args:
        if genre == "fiction":
            fiction_books.append(title)
        elif genre == "non_fiction":
            non_fiction_books.append(title)

    # Process the keyword arguments (ISBNs and book titles)
    for isbn, title in kwargs.items():
        if title in fiction_books:
            served_fiction_books.append(f"{isbn}#{title}")
        elif title in non_fiction_books:
            served_non_fiction_books.append(f"{isbn}#{title}")

    # Sort the books accordingly
    served_fiction_books = sorted(served_fiction_books, key=lambda x: x.split('#')[0])
    served_non_fiction_books = sorted(served_non_fiction_books, key=lambda x: x.split('#')[0], reverse=True)

    # Output formatting
    result = []
    if served_fiction_books:
        result.append("Fiction Books:")
        for book in served_fiction_books:
            result.append(f"~~~{book}")

    if served_non_fiction_books:
        result.append("Non-Fiction Books:")
        for book in served_non_fiction_books:
            result.append(f"***{book}")

    return "\n".join(result)


