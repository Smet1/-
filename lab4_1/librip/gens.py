import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    x = 0
    # c = {}
    assert len(args) > 0
    while x < len(items):
        b = dict.fromkeys(args)
        for a in args:
            try:
                b[a] = items[x][a]
            except:
                # if b[a] == 'None':
                b.pop(a)
        if not b:
            pass
        else:
            yield b
        x += 1
        # return c

        # print(args[0])
        # print(args[1])
        # Необходимо реализовать генератор


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    # pass
    arr = [random.choice(range(begin, end + 1)) for x in range(num_count)]
    return arr
    # Необходимо реализовать генератор
