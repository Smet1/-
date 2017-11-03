import requests
from Base_Client import BaseClient
import datetime
import json

class UserId(BaseClient):
    BASE_URL = 'http://api.vk.com/method/'
    method = 'users.get'
    http_method = None

    def __init__(self, name):
        self.name = name

    def get_params(self):
        return 'user_ids=' + self.name

    def response_handler(self, response):
        a = json.loads(response.text)
        b = a['response'][0]
        return b['id']

    def _get_data(self, method):
        response = None
        response = requests.get(self.BASE_URL + method + '?' + self.get_params()+'&v=5.68')
        return self.response_handler(response)