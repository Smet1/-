import random
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators1 import Unique as unique

if __name__ == '__main__':

    path = 'data_light_cp1251.json'
    # 'D:\Учеба\5 сем\РИП\lab4\ex-lab4-master\data_light.json'

    # Здесь необходимо в переменную path получить
    # путь до файла, который был передан при запуске

    with open(path) as f:
        data = json.load(f)


    # Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
    # Важно!
    # Функции с 1 по 3 дожны быть реализованы в одну строку
    # В реализации функции 4 может быть до 3 строк
    # При этом строки должны быть не длиннее 80 символов

    @print_result
    def f1(arg):
        return list([x for x in unique([i['job-name'] for i in arg], ignore_case=1)])


    @print_result
    def f2(arg):
        return list(filter(lambda x: 'программист' in x, arg))


    @print_result
    def f3(arg):
        return list(map(lambda x: x + ' с опытом Python', arg))


    @print_result
    def f4(arg):
        sal_list = list(gen_random(100000, 200000, len(arg)))
        work_list = iter(map(lambda x: x + ", зарплата", arg))
        return ["{} {} {}".format(work, sal, 'руб.') for (work, sal) in zip(work_list, sal_list)]



    with timer():
        f4(f3(f2(f1(data))))
