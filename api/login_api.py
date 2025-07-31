from api.register_api import RegisterApi
from models.user_model import LoginModel
from dataclasses import asdict


class LoginApi(RegisterApi):
    def __init__(self):
        super().__init__()

    def login(self, login_model: LoginModel):
        self.post(endpoint="/auth/login", body=asdict(login_model))

