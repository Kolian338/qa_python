from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # проверка метода init для books_rating
    def test_books_rating_create_dictionary_is_created(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        assert type(collector.get_books_rating()) is dict

    # проверка метода init для favorites
    def test_favorites_create_list_is_created(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        assert type(collector.get_list_of_favorites_books()) is list

    # рейтинг устанавливается = 1 по умолчанию, при добавлении книги
    def test_add_new_book_default_rating_1(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавили книгу
        book_name = 'Загадочные баги'
        collector.add_new_book(book_name)

        assert collector.get_book_rating(book_name) == 1

    # одна книга добавляется только один раз
    def test_add_new_book_when_add_same_book_dont_added(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавили книгу
        book_name = 'Таинственная пропажа призрака'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)

        assert len(collector.get_books_rating()) == 1

    # можно установить рейтинг книге
    def test_set_book_rating_set_rating_2(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавили книгу
        book_name = 'Возвращение загадочника'
        collector.add_new_book(book_name)

        # устанавливаем рейтинг книге
        collector.set_book_rating(book_name, 2)

        assert collector.get_book_rating(book_name) == 2

    # нельзя установить рейтинг книге если её нет в словаре
    def test_set_book_rating_can_not_rate_book_that_does_not_exist(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # создаем несуществующую книгу
        book_name = 'Несуществующая книга'

        # устанавливаем рейтинг книге которой нет в словаре
        collector.set_book_rating(book_name, 1)

        assert book_name not in collector.get_books_rating()

    # Нельзя выставить рейтинг меньше 1
    def test_set_book_rating_when_rating_less_1_can_not_set(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавили книгу
        book_name = 'Бэтмен'
        collector.add_new_book(book_name)

        # устанавливаем рейтинг = 0
        collector.set_book_rating(book_name, 0)

        assert collector.get_book_rating(book_name) != 0

    # Нельзя выставить рейтинг больше 10
    def test_set_book_rating_when_rating_more_10_can_not_set(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавили книгу
        book_name = 'Хоббиты и тайная комната'
        collector.add_new_book(book_name)

        # устанавливаем рейтинг = 11
        collector.set_book_rating(book_name, 11)

        assert collector.get_book_rating(book_name) != 11

    # нет рейтинга у несуществующей книги
    def test_get_book_rating_no_exist_book_has_no_rating(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        assert collector.get_book_rating('Несуществующая книга') is None

    # можно получить список книг по рейтингу от 1 до 10
    def test_get_books_with_specific_rating_rated_book_list_from_1_to_10_can_get(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книги
        book1_name = 'Тестовая книга №1'
        book2_name = 'Тестовая книга №2'
        collector.add_new_book(book1_name)
        collector.add_new_book(book2_name)

        # устанавливаем рейтинг
        collector.set_book_rating(book1_name, 1)
        collector.set_book_rating(book2_name, 10)

        assert collector.get_books_with_specific_rating(10)[-1] == book2_name

        # проверка на словарь
    def test_get_books_rating_dictionary_is_not_empty(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) != 0

    # Добавление книги в избранное
    def test_add_book_in_favorites_add_book_book_added_to_favorites(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)

        # добавляем книгу в избранное
        collector.add_book_in_favorites(book_name)

        assert book_name in collector.get_list_of_favorites_books()

    # Нельзя добавить книгу в избранное, если её нет в словаре books_rating
    def test_add_book_in_favorites_no_exist_book_not_added_to_favorites(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу в избранное
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_book_in_favorites(book_name)

        assert book_name not in collector.get_list_of_favorites_books()

    # Проверка удаления книги из избранного
    def test_delete_book_from_favorites_book_delete_book_is_deleted(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)

        # добавляем книгу в Избранное
        collector.add_book_in_favorites(book_name)

        # удаляем книгу из избранного
        collector.delete_book_from_favorites(book_name)

        assert book_name not in collector.get_list_of_favorites_books()
