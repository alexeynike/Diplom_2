import allure
from pygments.lexers import data

from api.base_api import BaseApi
from models.user_model import UserModel
from dataclasses import asdict


class RegisterApi(BaseApi):
    def register(self, user_model:UserModel):
        self.post(endpoint="/auth/register", body=asdict(user_model))

    @allure.step("Проверка что access token в теле ответа")
    def assert_access_token(self):
        assert "Bearer" in self.get_data(["accessToken"])

    @allure.step("Проверка что refresh token в теле ответа")
    def assert_refresh_token(self):
        assert len(self.get_data(["refreshToken"]))

    @allure.step("Проверка что пользователь успешно зарегистрирован")
    def assert_registered_user(self, user_modal: UserModel):
        data = self.get_data(["user"])
        assert data["email"] == user_modal.email
        assert data["name"] == user_modal.name
