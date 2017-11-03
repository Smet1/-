import inspect
# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
# Пример из ex_4.py:
# @print_result
# def test_1():
#     return 1
#
# @print_result
# def test_2():
#     return 'iu'
#
# @print_result
# def test_3():
#     return {'a': 1, 'b': 2}
#
# @print_result
# def test_4():
#     return [1, 2]
#
# test_1()
# test_2()
# test_3()
# test_4()
#
# На консоль выведется:
# test_1
# 1
# test_2
# iu
# test_3
# a = 1
# b = 2
# test_4
# 1
# 2
import traceback


def print_result(func_to_decorate):
    def decorated_func(*args):
        # func_to_decorate()
        print(func_to_decorate.__name__)
        func_to_decorate(*args)
        t = func_to_decorate(*args)
        if type(t) is dict:
            for key in t.keys():
                print('{} = {}'.format(key, t[key]))
        else:
            if type(t) is list:
                for values in t:
                    print(values)
            else:
                print(t)
        return t
    return decorated_func

