from dataclasses import dataclass


@dataclass
class UserModel:
    email: str
    password: str
    name: str


@dataclass
class LoginModel(UserModel):
    name: str | None = None
