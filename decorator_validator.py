"""Файл валидатор"""
from typing import Callable, Any
import re

import jsonschema
from jsonschema import validate

from json_schema import SCHEMA
from jsoner import json_messager
from service import name_randomizer


def input_validation(input_json: dict = json_messager(), schema: dict = SCHEMA) -> Any:
    """Валидатор входящего JSON."""
    print(input_json)
    try:
        validate(input_json, schema)
        print('Валидный входящий json')
        return input_json
    except jsonschema.exceptions.ValidationError:
        print('Невалидный json')
        return 'Невалидный json'


input_validation()

#
# def validator(function, input_validation: Callable=input_validation()) -> Any:
#     pass




def string_checker(str):
    """проверка на кириллические символы."""
    result = re.fullmatch('^[а-яА-я]+\s[а-яА-я]+\s[а-яА-я]+$',str) #проверятор ФИО
    return result.group(0)

# print(string_checker(name_randomizer()))