#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3]
data2 = gen_random(1, 10, 10)
data3 = ['a', 'A', 'b', 'B', 'a']

if __name__ == '__main__':
    a = Unique(data3, ignore_case=1)
    for i in a:
        print(i, end=' ')
    # print('\n', data3)
    print()
    b = Unique(gen_random(1, 10, 10))
    for i in b:
        print(i, end=' ')
    # Реализация задания 2
