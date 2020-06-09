"""Файл для работы с JSON."""
import random
import re
from service import approve_cod, id_randomizer, address_creater, status_randomizer, weight_generator, create_time, \
    name_randomizer


def json_messager() -> dict:
    """Тестовая функция-генерирует тестовые JSON, как валидный так и нет."""
    random_event = random.randint(1, 6)
    if random_event > 2:
        json_valid = {
            "id": id_randomizer(),
            "status": status_randomizer()
        }
        return json_valid

    elif random_event == 2:
        json_invalid = {
            "id": approve_cod(),
            "status": create_time()
        }
        return json_invalid

    else:
        json_invalid = {
            "id": id_randomizer(),
            "status": status_randomizer(),
            "additional_tag": address_creater(),
            "Норм да ": True
        }

        return json_invalid
