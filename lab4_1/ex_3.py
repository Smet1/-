#!/usr/bin/env python3

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

# Реализация задания 3
if __name__ == '__main__':
    print(list(sorted(data, key=lambda num: abs(num))))
