# Итератор для удаления дубликатов
class Unique(object):
    flag = False

    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False

        self.flag1 = True
        self.lst = items[:]
        self.index = 0
        if len(kwargs) == 1:
            if kwargs['ignore_case']:
                self.flag = True

        if self.flag == True and type(items[0]) is str:
            for x in range(len(items)):
                self.lst[x] = self.lst[x].lower()
        print(items)

        self.lst.sort()

    def __next__(self):
        # Нужно реализовать __next__
        if self.index == len(self.lst) - 1 or self.lst[self.index] == self.lst[len(self.lst) - 1]:
            raise StopIteration

        if self.index == 0 and self.flag1:
            self.flag1 = False
            return self.lst[self.index]

        self.index = self.index + self.lst.count(self.lst[self.index])

        # a = self.lst.count(self.lst[self.index])

        return self.lst[self.index]

    def __iter__(self):
        return self
