class Book:
    """A class to represent a book and track the total number of books created.
    Attributes:
        title (str): The title of the book.
    """
    total_books: int = 0

    def __init__(self, title: str):
        self.title = title
        Book.increment_book_count()


    @classmethod
    def increment_book_count(cls):
        """Increment the total_books count by 1."""
        cls.total_books += 1


if __name__ == '__main__':
    book1 = Book("Harry Potter")
    book2 = Book("Indus Journey")
    book3 = Book("Docker")

    print(f"Total books created: {Book.total_books}")
