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
        self.lst_new = set()
        self.index = 0
        if len(kwargs) == 1:
            if kwargs['ignore_case']:
                self.flag = True

        if self.flag is True and type(items[0]) is str:
            for x in range(len(items)):
                self.lst[x] = self.lst[x].lower()
        print(items)

        # self.lst.sort()

    def __next__(self):
        # Нужно реализовать __next__
        if self.index == len(self.lst):
            # print(self.lst_new)
            raise StopIteration

        if self.lst[self.index] in self.lst_new:
            self.index += 1
            pass

        else:
            self.lst_new.add(self.lst[self.index])
            print(self.lst[self.index], end=' ')

        self.__next__()
        # return self.lst[self.index]

        # print(self.lst[self.index], end=' ')

    def __iter__(self):
        return self
