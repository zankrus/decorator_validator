"""Файл валидатор"""
from typing import Callable, Any, Optional, Match
import re

import jsonschema
from jsonschema import validate
from json_schema import SCHEMA
from jsoner import json_messager


def input_validation(input_json: dict, schema: dict = SCHEMA) -> Any:
    """Валидатор входящего JSON."""
    print('Входящий JSON : ' + str(input_json))
    try:
        validate(input_json, schema)
        return input_json
    except jsonschema.exceptions.ValidationError:
        print('Json прошел проверку валидации схемы')
        raise Exception('InputParameterVerificationError')


def output_validation(str):
    """Проверка на название статуса."""
    result = re.fullmatch("(?i)(\W|^)(В\sобработке|Доставляется|Доставлено)(\W|$)", str)
    if bool(result):
        print('Проверка соответствия статуса регулярному выражению прошла успешно')
        return result
    else:
        print('Проверка соответствия статуса регулярному выражению провалена')
        raise Exception('ResultVerificationError')


def default_func():
    """Функция при провале повторений."""
    print('Функция провалена')


class ResultVerificationError(BaseException):
    pass


class InputParameterVerificationError(BaseException):
    pass


def decorator(input_validator: Callable, result_validation: Callable, on_fail_repeat_times: int = 1,
              default_behaviour: Callable = None):
    def outer_wrapper(function):
        def wrapper(*args,**kwargs):
            print('Начало валидации')
            for i in range(on_fail_repeat_times):
                try:
                    input_validator(*args, **kwargs)
                    result_validation(dict(*args, ** kwargs)['status'])
                except InputParameterVerificationError :
                    print('Ошибка валидации схемы')
                except ResultVerificationError:
                    print('Ошибка валидации статуса')

            print('Валидация успешно проведена')
            print('')
            print('Выполняется основная функция')
            res = function(*args)
            return res
        return wrapper
    return outer_wrapper


@decorator(
    input_validator=input_validation,
    result_validation=output_validation,
    on_fail_repeat_times=2,
    default_behaviour=default_func)
def homework_function(json: dict) -> str:
    """Функция которая выдает сообщение о номере заказа и статусе."""
    string = 'Номер заказа ' + str(json['id']) + ' .Статус заказа : ' + str(json['status'])
    print(string)
    return string


homework_function(json_messager())
