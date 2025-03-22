import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    #1 тест на проверку, что books_genre инициализируется как пустой словарь
    def test_init_books_genre_is_empty_dictionary(self,collector):
        assert collector.books_genre == {}

    #2 тест на проверку, что favorites инициализируется как пустой список
    def test_init_favorites_is_empty_list(self,collector):
        assert collector.favorites == []

    #3 тест на проверку, что genre инициализируется с правильными значениями
    def test_init_genre_has_correct_values(self, collector):
       assert collector.genre ==  ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    #4 тест на проверку, что genre_age_rating инициализируется с правильными значениями
    def test_init_genre_age_rating_has_correct_values(self, collector):
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    #5 тест на добавление одной книги
    def test_add_new_book_add_one_book(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        assert 'Гордость и предубеждение' in collector.books_genre

    #6 тест на проверку что, не добавляются книги с пустым названием и очень длинным названием
    @pytest.mark.parametrize('name', ['', 'Странная история доктора Джекила и мистера Хайда'])
    def test_add_new_book_not_added_invalid_name(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.books_genre) == 0

    #7 тест на установления известного жанра книги
    def test_set_book_genre_set_valid_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Комедии')
        assert collector.get_book_genre('Гордость и предубеждение') == 'Комедии'

    #8 тест на установления неизвестного жанра книги
    def test_set_book_genre_set_invalid_genre(self, collector):
        collector.add_new_book('Поющие в терновнике')
        collector.set_book_genre('Поющие в терновнике', 'Драмы')
        assert collector.get_book_genre('Поющие в терновнике') == ''

    #9 тест на получения жанра книги
    @pytest.mark.parametrize('genre', ['Детективы', 'Ужасы', 'Комедии'])
    def test_get_book_genre_return_correct_genre(self, collector, genre):
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', genre)
        assert collector.get_book_genre('Гордость и предубеждение') == genre

    #10 тест на вывод списка книг с определённым жанром
    @pytest.mark.parametrize('spec_genre', ['Детективы', 'Ужасы', 'Комедии'])
    def test_get_books_with_specific_genre_return_correct_list(self, collector, books_dict_1, spec_genre):
        books_with_spec_genre = []
        for name, genre in books_dict_1.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
            if genre == spec_genre:
                books_with_spec_genre.append(name)
        assert collector.get_books_with_specific_genre(spec_genre) == books_with_spec_genre

    #11 тест на получение словаря books_genre
    def test_get_books_genre_return_correct_dictionary(self, collector, books_dict_2):
        for name, genre in books_dict_2.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert collector.get_books_genre() == books_dict_2

    #12 тест на возвращение книг, подходящих детям
    def test_get_books_for_children_return_correct_list(self, collector, books_dict_1):
        children_books = []
        for name, genre in books_dict_1.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
            if (genre not in collector.genre_age_rating) and (genre in collector.genre):
                children_books.append(name)
        assert collector.get_books_for_children() == children_books

    #13 тест на добавление книги в Избранное
    @pytest.mark.parametrize('name', ['Вий','Нос','Мёртвые души','Ревизор'])
    def test_add_book_in_favorites_add_one_book(self, collector, name):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

    #14 тест на удаление книги из Избранного
    @pytest.mark.parametrize('name', ['Вий', 'Нос', 'Мёртвые души', 'Ревизор'])
    def test_delete_book_from_favorites_delete_one_book(self, collector, name):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.get_list_of_favorites_books()

    #15 тест на получение списка Избранного
    def test_get_list_of_favorites_books_return_correct_list(self, collector, books_dict_1):
        favorite_books = []
        for name, genre in books_dict_1.items():
            collector.add_new_book(name)
            if (genre not in collector.genre_age_rating) and (genre in collector.genre):
                favorite_books.append(name)
                collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == favorite_books
