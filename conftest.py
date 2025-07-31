import pytest
from faker import Faker

from api.login_api import LoginApi
from api.order_api import OrderApi
from api.register_api import RegisterApi
from api.update_user_api import UpdateUserAPI
from models.user_model import UserModel, LoginModel
from api.base_api import BaseApi

@pytest.fixture
def register_api():
    return RegisterApi()

@pytest.fixture
def login_api():
    return LoginApi()

@pytest.fixture
def update_user_api():
    return UpdateUserAPI()

@pytest.fixture
def order_api():
    return OrderApi()

@pytest.fixture
def get_user():
    fake = Faker()
    return UserModel(email=fake.email(), password=fake.password(), name=fake.name())

@pytest.fixture
def default_user():
    return UserModel(email="test@test.md", password="qwerty123", name="test")

@pytest.fixture
def registered_user():
    return LoginModel(email="test@test.md", password="qwerty123")


@pytest.fixture
def login_user(register_api, get_user):
    register_api.register(get_user)
    BaseApi.headers.update({"Authorization": register_api.get_data(["accessToken"])})
    return get_user

@pytest.fixture
def get_burger_ingredients():
    return {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa72"]
    }

@pytest.fixture
def make_default_order(order_api, get_burger_ingredients):
    order_api.make_order(get_burger_ingredients)