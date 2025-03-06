import pytest

import data
import helper


@pytest.fixture
def book():
    book = BooksCollector()
    return book

@pytest.fixture
def book_with_favorite(book):
    book.add_book_to_favorite(helper.generate_random_book())
    return book