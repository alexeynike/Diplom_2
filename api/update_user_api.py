import allure

from api import register_api, login_api
from api.base_api import BaseApi
from api.login_api import LoginApi
from models.user_model import UserModel
from dataclasses import asdict


class UpdateUserAPI(BaseApi):
    def update_user(self, user_model: UserModel):
        self.patch(endpoint="/auth/user", body = asdict(user_model))

    @allure.step("Проверка что имя пользователя изменено")
    def assert_user_name(self, user_name):
        assert self.get_data(["user", "name"]) == user_name
        