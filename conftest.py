import pytest
from main import BooksCollector
from test_data import BOOKS_DATA, FAVORITES_BOOKS

@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def more_books(collector):
    for name, genre in BOOKS_DATA:
        collector.add_new_book(name)
        if genre:
            collector.set_book_genre(name, genre)
    return collector

@pytest.fixture
def collector_favorites_book(collector):
    for book in FAVORITES_BOOKS:
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
    return collector