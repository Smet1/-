import json
from datetime import datetime, date, time
from Friends import Friends
from UserId import UserId

if __name__ == '__main__' :
    params = {'https://api.vk.com/method/','friends.get','?user_id=88459587&v=5.52'}
    name = input()
    id_name = UserId(str(name))
    fr = Friends(str(id_name._get_data('users.get')))
    ages = {}
    ages = fr._get_data('friends.get')
    statistic = sorted(ages.items(), key=lambda x: x[0])
    for i in statistic:
        print('{} {}'.format(i[0], i[1]))



    a = UserId('taron997')
    b = a._get_data('users.get')
    print(b)

    fr = Friends(str(b))
    ages = {}
    ages = fr._get_data('friends.get')
    statistic = sorted(ages.items(), key=lambda x: x[0])
    for i in statistic:
        print('{} => {}'.format(i[0], i[1]))