from UserId import UserId
from Friends import Friends
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    # обычная гистограмма
    name = UserId('taron997').execute()
    print(name)
    fr = Friends(name).execute()
    statistic = sorted(fr.items(), key=lambda x: x[0])
    for i in statistic:
        print('{} => {}'.format(i[0], i[1]))

    # гистограмма matplotlib
    fr_math = Friends(name).execute_for_math()
    # print(fr_math)
    plt.hist(fr_math, 150)
    plt.show()
