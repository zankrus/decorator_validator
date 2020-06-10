"""Файл запуска проверки."""
from decorator_validator import homework_function
from jsoner import json_messager

"""Установлены параметры декоратора"""
"""@decorator("""
"""input_validator=input_validation,"""
"""result_validation=output_validation,"""
"""on_fail_repeat_times=5,"""
"""default_behaviour=default_func)."""
""" Функция Json_messager гененирует JSON"""
""" 40% невалидные , 60% валидные"""
if __name__ == '__main__':
    for i in range(5):
        homework_function(json_messager())
