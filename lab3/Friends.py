import datetime
import json
from datetime import datetime
import requests
from Base_Client import BaseClient
import numpy as np


class Friends(BaseClient):
    BASE_URL = 'http://api.vk.com/method/'
    method = 'friends.'
    http_method = 'get'

    def __init__(self, id):
        self.id = str(id)

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
                if age not in ages:
                    ages[age] = ''
                ages[age] += '#'
            except:
                pass
        return ages

    def _get_data(self, method, http_method):
        response = None
        response = requests.get(self.BASE_URL + method + http_method + '?' + self.get_params() + '&fields=bdate&v=5.68')
        # print(response)
        return self.response_handler(response)

    def execute_for_math(self):
        return self._get_data_math(
            self.method,
            http_method=self.http_method
        )

    def _get_data_math(self, method, http_method):
        response = None
        response = requests.get(self.BASE_URL + method + http_method + '?' + self.get_params() + '&fields=bdate&v=5.68')
        # print(response)
        return self.response_handler_math(response)

    def response_handler_math(self, response):
        ages = []
        cur_date = datetime.now()
        a = json.loads(response.text)
        e = int(a['response']['count'])
        for i in range(e):
            d = a['response']['items'][i]
            try:
                date1 = datetime.strptime(d['bdate'], '%d.%m.%Y')
                delta = (cur_date - date1).days
                age = delta // 365.25
                ages.append(age)
            except:
                continue
        return ages
        # np.array(ages)
