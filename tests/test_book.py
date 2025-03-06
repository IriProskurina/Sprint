import pytest

import data


class TestClass:

    def test_add_book_to_favorite(self, book):
        book.add_book_to_favorite(data.BOOK_TITLE)
        favorite = book.get_favorite_books()
        assert data.BOOK_TITLE in favorite

    def test_add_book_favorite_len(self, book_with_favorite):
        book_with_favorite.add_book_to_favorite(data.BOOK_TITLE)
        favorite = book.get_favorite_books()
        assert len(favorite) > 1

    @pytest.mark.parametrize(
        'name', 'books_count',
        [
            (['Книга 1', 'Что делать если ваш кот хочет вас убить'], 2),
            ([ 'Что делать если ваш кот хочет вас убить'], 1),
            ([], 0),
        ]
    )
    def test_add_book_to_favorite_list(self,book,name,books_count):
        for book_name in name:
            book.add_book_to_favorite(book_name)
        favorite = book.get_favorite_books()
        assert len(favorite) == books_count