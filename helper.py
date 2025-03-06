import random

from faker import Faker

def generate_random_book():
    titles = ['Книга 1', 'Что делать если ваш кот хочет вас убить', 'Книга 3']
    return random.choice(titles)

fake = Faker()
def generate_random_book_title():
