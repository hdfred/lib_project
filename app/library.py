class Library:
    def __init__(self):
        self._books = []

    def add_book(self, title: str):
        if not title:
            raise ValueError('Title cannot be empty')
        if title in self._books:
            raise ValueError('Book already exists')
        self._books.append(title)

    def remove_book(self, title: str):
        if title not in self._books:
            raise ValueError('Book not found')
        self._books.remove(title)

    def search(self, query: str):
        return [b for b in self._books if query.lower() in b.lower()]
    
    def list_books(self):
        return list(self._books)