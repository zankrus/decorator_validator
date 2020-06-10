"""Файл валидатор. Тут хранятся функции, которые принимает декоратор."""
from typing import Callable, Any
import re

import jsonschema
from jsonschema import validate

from json_schema import SCHEMA


def input_validation(input_json: dict, schema: dict = SCHEMA) -> Any:
    """Валидатор входящего JSON."""
    print('Входящий JSON : ' + str(input_json))
    try:
        validate(input_json, schema)
        return input_json
    except jsonschema.exceptions.ValidationError:
        print('Json  провалил проверку валидации схемы')
        raise Exception('InputParameterVerificationError')


def output_validation(str: str) -> bool:
    """Проверка на название статуса."""
    result = re.fullmatch(r"(?i)(\W|^)(В\sобработке|Доставляется|Доставлено)(\W|$)", str)
    if bool(result):
        print('Проверка соответствия статуса регулярному выражению прошла успешно')
        return bool(result)
    else:
        print('Проверка соответствия статуса регулярному выражению провалена')
        raise Exception('ResultVerificationError')


def default_func() -> None:
    """Функция при провале повторений."""
    print('Количество попыток превышено. Запущена дефолт-функция')


def decorator(input_validator: Callable, result_validation: Callable, on_fail_repeat_times: int = 1,
              default_behaviour: Callable = None) -> Callable:
    """Функция декоратор."""
    if on_fail_repeat_times == 0:
        raise Exception('Parameter on_fail_repeat_times cannot be zero')

    def outer_wrapper(function: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print('')
            print('')
            print('Начало валидации')
            if on_fail_repeat_times < 0:
                while True:
                    try:
                        input_validator(*args, **kwargs)
                        result_validation(dict(*args, **kwargs)['status'])
                        print('Валидация успешно проведена')
                        break
                    except Exception:
                        print('Ошибка валидации')

            else:
                for i in range(1, on_fail_repeat_times + 1):
                    print('Попытка валидации № {}'.format(i))
                    try:
                        schema_result = input_validator(*args, **kwargs)
                        re_result = result_validation(dict(*args, **kwargs)['status'])
                        if schema_result and re_result:
                            print('Валидация успешно проведена')
                            break
                    except Exception:
                        print('Ошибка валидации')
                        if default_behaviour is not None and i == on_fail_repeat_times:
                            default_behaviour()
                            return False
                        elif i == on_fail_repeat_times:
                            return False
            print('')
            print('Выполняется основная функция')
            res = function(*args)
            return res

        return wrapper

    return outer_wrapper


@decorator(
    input_validator=input_validation,
    result_validation=output_validation,
    on_fail_repeat_times=5,
    default_behaviour=default_func)
def homework_function(json: dict) -> str:
    """Функция которая выдает сообщение о номере заказа и статусе."""
    string = 'Номер заказа ' + str(json['id']) + ' .Статус заказа : ' + str(json['status'])
    print(string)
    return string
