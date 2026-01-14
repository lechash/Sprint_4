import pytest
from main import BooksCollector

class TestBooksCollector:

    # Тест добавления книг
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # тест на проверку длины названия книги
    @pytest.mark.parametrize('book_name, expected_result', [
        ('Супердлинное название книги превышающее лимит в сорок символов', False),
        ('Мастер и Маргарита', True),
        ('', False),  # пустое название
        ('А', True),  # 1 символ
        ('К' * 40, True),  # ровно 40 символов (граница)
        ('К' * 41, False),  # 41 символ (за границей)
    ])
    def test_add_new_book_name_length_validation(self, collector, book_name, expected_result):
        collector.add_new_book(book_name)
        assert (book_name in collector.get_books_genre()) == expected_result

    # тест на установку жанра
    @pytest.mark.parametrize('book_name, genre, expected_genre', [
        ('Новая книга', 'Фантастика', 'Фантастика'),  # Корректный жанр
        ('Война и мир', 'Роман', ''),  # Некорректный жанр (не в списке genre)
    ])
    
    def test_set_book_genre_valid_genre(self, collector, book_name, genre, expected_genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected_genre
    
    
    # тест на жанр книги по ее имени
    def test_get_book_genre_existing_book(self, more_books):
        assert more_books.get_book_genre('Звездные войны') == 'Фантастика'


    def test_get_book_genre_nonexistent_book(self, collector):
        assert collector.get_book_genre('Несуществующая книга') is None

    # тест на список книг с определённым жанром
    def test_get_books_with_specific_genre_existing(self, more_books):
        books = more_books.get_books_with_specific_genre('Фантастика')
        assert 'Звездные войны' in books and len(books) == 1

    def test_get_books_with_specific_genre_invalid(self, more_books):
        books = more_books.get_books_with_specific_genre('Несуществующий жанр')
        assert books == []

    # тест на получение словаря books_genre
    def test_get_books_genre_returns_current_state(self, more_books):
        expected = {
            'Звездные войны': 'Фантастика',
            'Оно': 'Ужасы',
            'Агата Кристи': 'Детективы',
            'Мамонтенок': 'Мультфильмы',
            'Живая шляпа': 'Комедии',
            'Просто книга': ''
        }
        assert more_books.get_books_genre() == expected
       

    # тест на книги, подходящие детям
    def test_get_books_for_children_not_kid_friendly(self, more_books):
        children_books = more_books.get_books_for_children()
        assert 'Оно' not in children_books  # Ужасы — не для детей


    def test_get_books_for_children_kid_friendly(self, more_books):
        children_books = more_books.get_books_for_children()
        assert 'Мамонтенок' in children_books  # Мультфильмы — для детей 

   
    # тест на добавление в избранное
    def test_add_book_in_favorites_one_book(self, collector):
        collector.add_new_book('Новая книга')
        collector.add_book_in_favorites('Новая книга')
        assert 'Новая книга' in collector.get_list_of_favorites_books()
        

    # тест на удаление из избранного
    def test_delete_book_from_favorites_one_book(self, collector_favorites_book):
        collector_favorites_book.delete_book_from_favorites('Оно')
        assert 'Оно' not in collector_favorites_book.get_list_of_favorites_books()
        

    # тест на получение списка избранного
    def test_get_list_of_favorites_books_return_all(self, collector_favorites_book):
        favorites = collector_favorites_book.get_list_of_favorites_books()
        expected = ['Звездные войны', 'Оно', 'Агата Кристи']
        assert favorites == expected
        
