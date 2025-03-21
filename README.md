класс TestBooksCollector содержит следующие тесты для проверки методов класса BooksCollector:

test_init_books_genre_is_empty_dictionary - тест на проверку, что books_genre инициализируется как пустой словарь
test_init_favorites_is_empty_list - тест на проверку, что favorites инициализируется как пустой список
test_init_genre_has_correct_values - тест на проверку, что genre инициализируется с правильными значениями
test_init_genre_age_rating_has_correct_values - тест на проверку, что genre_age_rating инициализируется с правильными значениями
   
test_add_new_book_add_one_book -  тест на добавление одной книги
test_set_book_genre_set_valid_genre - тест на установления известного жанра книги
test_set_book_genre_set_invalid_genre - тест на установления неизвестного жанра книги
test_get_book_genre_return_correct_genre - тест на получения жанра книги
test_get_books_with_specific_genre_return_correct_list - тест на вывод списка книг с определённым жанром
test_get_books_genre_return_correct_dictionary - тест на получение словаря books_genre
test_get_books_for_children_return_correct_list - тест на возвращение книг, подходящих детям
test_add_book_in_favorites_add_one_book - тест на добавление книги в Избранное
test_delete_book_from_favorites_delete_one_book - тест на удаление книги из Избранного
test_get_list_of_favorites_books_return_correct_list - тест на получение списка Избранного
