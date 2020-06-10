"""Файл для хранения вспомогательных функций."""
import random
import string
from typing import Generator

from faker import Faker

fake = Faker("ru_RU")


def approve_cod() -> str:
    """Функция генерирует код подтверждения."""
    password = ''
    for i in range(1, 3):
        password += random.choice(string.ascii_uppercase)
    for i in range(3, 6):
        password += random.choice(string.digits)
    for i in range(7, 11):
        password += random.choice(string.ascii_lowercase)
    for i in range(11, 12):
        password += random.choice('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    return str(password)


def address_creater() -> str:
    """Функция генерации случайного адреса."""
    address = str('Улица ' + str(fake.word()).capitalize() + ', ' + str(fake.random_int(1, 150)))
    return address


def status_randomizer() -> str:
    """Генерация случайного статуса посылки."""
    list_of_statuses = ['В обработке', 'Доставляется ', 'Доставлено', 'НЕГАТИВНЫЙ СТАТУС', 'ARARARARA']
    status = random.choice(list_of_statuses)
    return status


def weight_generator() -> int:
    """Генерация веса посылки."""
    weight = fake.random_int(100, 10000)
    return weight


def create_time() -> str:
    """Генерация времени создания запроса."""
    time = fake.date_time_this_year()
    return time


def id_randomizer() -> str:
    """Генератор айди отправления."""
    def id_generator() -> Generator:
        for i in string.ascii_uppercase:
            for digit in range(1, 10):
                id = ''
                id += i
                id += str(digit)
                yield id

    list_of_id = [x for x in id_generator()]
    return random.choice(list_of_id)


def name_randomizer() -> str:
    """рандом имени."""
    name = fake.name()
    return name
