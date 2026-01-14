import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def more_books(collector):
    books = [
        ('Звездные войны', 'Фантастика'),
        ('Оно', 'Ужасы'),
        ('Агата Кристи', 'Детективы'),
        ('Мамонтенок', 'Мультфильмы'),
        ('Живая шляпа', 'Комедии'),
        ('Просто книга', '')  # без жанра
    ]
    for name, genre in books:
        collector.add_new_book(name)
        if genre:
            collector.set_book_genre(name, genre)
    return collector

@pytest.fixture
def collector_favorites_book(collector):
    books = ['Звездные войны', 'Оно', 'Агата Кристи']
    for book in books:
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
    return collector