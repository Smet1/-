import requests
from Base_Client import BaseClient
import datetime
import json
from datetime import datetime, date, time

#id88459587

class Friends(BaseClient):
    BASE_URL = 'http://api.vk.com/method/'
    method = 'friends.get'
    http_method = None

    def __init__(self, id):
        self.id = id

    def get_params(self):
        return 'user_id=' + self.id

    def response_handler(self, response):
        ages = {}
        cur_date = datetime.now()
        a = json.loads(response.text)
        e = int(a['response']['count'])
        for i in range(e):
            d = a['response']['items'][i]
            try:
                date1 = datetime.strptime(d['bdate'], '%d.%m.%Y')
                delta = (cur_date - date1).days
                age = delta // 365.25
                if (age not in ages):
                    ages[age] = ''
                ages[age] += '#'
                # print(age)

            except:
                None
        return ages

    def _get_data(self, method):
        response = None
        response = requests.get(self.BASE_URL + method + '?' + self.get_params()+'&fields=bdate&v=5.68')
        print(self.BASE_URL + method + '?' + self.get_params()+'&fields=bdate&v=5.68')
        return self.response_handler(response)