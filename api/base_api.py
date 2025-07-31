import requests
from helpers.logger import *
import allure


class BaseApi:
    headers = {}

    def __init__(self):
        self.base_url = "https://stellarburgers.nomoreparties.site/api"
        self.response = None

    def _request(self, method=None, endpoint=None, data=None, headers=None):
        if headers is not None:
            self.headers = headers
        logging_request(url=endpoint, method=method, data=data, headers=self.headers)
        self.response = requests.request(method=method, url=self.base_url + endpoint, json=data, headers=self.headers)
        logging_response(self.response)

    @allure.step("Отправить GET запрос на {endpoint}")
    def get(self, endpoint: str):
        return self._request(method="GET", endpoint=endpoint)

    @allure.step("Отправить POST запрос на {endpoint}")
    def post(self, endpoint, body):
        return self._request(method="POST", endpoint=endpoint, data=body)

    @allure.step("Отправить DELETE запрос на {endpoint}")
    def delete(self, endpoint: str):
        return self._request(method="DELETE", endpoint=endpoint)

    @allure.step("Отправить PUT запрос на {endpoint}")
    def put(self, endpoint, body):
        return self._request(method="PUT", endpoint=endpoint, data=body)

    @allure.step("Отправить PATCH запрос на {endpoint}")
    def patch(self, endpoint, body, headers=None):
        return self._request(method="PATCH", endpoint=endpoint, data=body, headers=headers)

    @allure.step("Получить данные из тела ответа по ключам: {keys}")
    def get_data(self, keys):
        body = self.response.json()
        try:
            for key in keys:
                body = body[key]
            return body
        except KeyError:
            raise KeyError(f"По ключу {keys} значение отсутствует")

    @allure.step("Проверка status cod: {expected_code}")
    def assert_status_code_is(self, expected_code):
        assert expected_code == self.response.status_code, f"ОР: статус код {expected_code}\nФР: статус код {self.response.status_code}"

    @allure.step("Тело ответа равно: {data}")
    def assert_body_is(self, data):
        assert self.response.json() == data, f"ОР: тело ответа равно: {data}\nФР: тело ответа: {self.response.json()}"

    @allure.step("Тело ответа содержит: {data}")
    def assert_body_have(self, data):
        assert self.response.json().get(data) is not None, f"ОР: Тело ответа содержит поле {data}\nФР: Тело ответа{self.response.json()}"

    @allure.step("Сообщение в теле ответа: {message}")
    def assert_response_message(self, message: str):
        assert self.get_data(["message"]) == message

    @allure.step("Succsess status в теле ответа: {status}")
    def assert_success_status(self, status=True):
        assert self.get_data(["success"]) == status
