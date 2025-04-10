import unittest
from unittest.mock import Mock
from library import Library
from library_repository import LibraryRepository

class TestLibraryInteractions(unittest.TestCase):
    def setUp(self):
        self.mock_repo = Mock(spec=LibraryRepository)
        self.library = Library(self.mock_repo)

    def test_borrow_book_calls_remove_book(self):
        self.mock_repo.remove_book.return_value = True

        result = self.library.borrow_book("Przykładowa książka")
        self.mock_repo.remove_book.assert_called_once_with("Przykładowa książka")
        self.assertTrue(result)

    def test_return_book_calls_add_book(self):
        self.library.return_book("Przykładowa książka", "Autor", 2023)
        self.mock_repo.add_book.assert_called_once_with("Przykładowa książka", "Autor", 2023)

    def test_list_books_calls_get_all_books(self):
        self.mock_repo.get_all_books.return_value = [("Przykładowa książka", {"author": "Autor", "year": 2023})]
        books = self.library.list_books()
        self.mock_repo.get_all_books.assert_called_once()
        self.assertEqual(books, [("Przykładowa książka", {"author": "Autor", "year": 2023})])

if __name__ == '__main__':
    unittest.main()
