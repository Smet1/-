import requests
import datetime

class BaseClient:
    # URL vk api
    BASE_URL = None
    # метод vk api
    method = None
    # GET, POST, ...
    http_method = None

    # Получение GET параметров запроса
    def get_params(self):
        return None

    # Получение данных POST запроса
    def get_json(self):
        return None

    # Получение HTTP заголовков
    def get_headers(self):
        return None

    # Склейка url
    def generate_url(self, method):
        return '{0}{1}'.format(self.BASE_URL, method)

    # Отправка запроса к VK API
    def _get_data(self, method, http_method):
        response = None

        # todo выполнить запрос

        return self.response_handler(response)

    # Обработка ответа от VK API
    def response_handler(self, response):
        return response

    # Запуск клиента
    def execute(self):
        return self._get_data(
            self.method,
            http_method=self.http_method
        )

class User(BaseClient):
    def __init__(self ,url, meth, http):
        self.BASE_URL = url
        self.method = meth
        self.http_method = http
    def get_params(self):
        return { self.BASE_URL, self.method, self.http_method}
    def generate_url(self):
        return '{0}{1}'.format(self.BASE_URL, self.method)


#id88459587

#class Get_id(base_client):
if __name__ == '__main__' :
    params = {'https://api.vk.com/method/','friends.get','?user_id=88459587&v=5.52'}
    a = User('https://api.vk.com/method/','users.get','?user_id=88459587&v=5.52');
    print(a.get_params());
    print(a.generate_url());
    print(a._get_data());