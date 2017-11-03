#!/usr/bin/env python3
from librip.gens import field, gen_random

goods = [
    {'title': 'Ковер', 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]
if __name__ == '__main__' :
    for i in field(goods, 'price', 'color', 'title'):
        print(i, end=' ')

    num_count = 5
    begin = 1
    end = 3
    a = gen_random(int(begin),int(end),int(num_count))
    print('\n',a)
# Реализация задания 1
