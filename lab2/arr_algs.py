def min(lst):
    minVal = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < minVal:
            minVal = lst[i]
    return minVal


def avg(lst):
    sum = 0
    for i in range(1, len(lst)):
        sum += lst[i]
    return sum / len(lst)


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, ]
    print(min(lst))
    print(avg(lst))
