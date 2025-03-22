from main import BooksCollector
import pytest


#создание объекта класса BooksCollector
@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()
    return collector

#создание тестового словаря книг, включающего неизвестные жанры
@pytest.fixture(scope='session')
def books_dict_1():
    books_dict = {'Убийство на поле для гольфа': 'Детективы',
                  'Убийство в Восточном экспрессе': 'Детективы',
                  'Дневник Бриджит Джонс': 'Комедии',
                  'Джейн Эйр': 'Мелодрамы',
                  'Дракула': 'Ужасы',
                  'Грозовой перевал': 'Романы',
                  'Люди, которые всегда со мной': 'Проза'}
    return books_dict

#создание тестового словаря книг, включающего только известные жанры
@pytest.fixture(scope='session')
def books_dict_2():
    books_dict = {'Убийство на поле для гольфа': 'Детективы',
                  'Солярис': 'Фантастика',
                  'Дневник Бриджит Джонс': 'Комедии',
                  'Три поросенка': 'Мультфильмы',
                  'Дракула': 'Ужасы',
                  'Оно': 'Ужасы',
                  '12 стульев': 'Комедии'}
    return books_dict
