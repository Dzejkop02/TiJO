from library_repository import LibraryRepository

class InMemoryRepository(LibraryRepository):
    def __init__(self):
        self.books = {}  # Słownik przechowujący książki

    def add_book(self, title: str, author: str, year: int):
        self.books[title] = {'author': author, 'year': year}

    def remove_book(self, title: str) -> bool:
        # jeśli istnieje
        if title in self.books:
            del self.books[title]
            return True
        return False

    def get_all_books(self) -> list:
        # krotki (tytuł, szczegóły książki)
        return [(title, info) for title, info in self.books.items()]
