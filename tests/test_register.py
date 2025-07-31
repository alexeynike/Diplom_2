import allure


class TestRegister:

    @allure.title("Регистрация пользователя")
    def test_register_user(self, register_api, get_user):
        get_user.email="test@test.md"
        get_user.password="qwerty123"
        get_user.name="test"
        register_api.register(get_user)
        register_api.assert_status_code_is(200)

    @allure.title("Проверка access токена")
    def test_access_token(self, register_api, get_user):
        register_api.register(get_user)
        register_api.assert_status_code_is(200)
        register_api.assert_access_token()

    @allure.title("Проверка refresh токена")
    def test_refresh_token(self, register_api, get_user):
        register_api.register(get_user)
        register_api.assert_status_code_is(200)
        register_api.assert_refresh_token()

    @allure.title("Проверка данных зарегистрированного пользователя")
    def test_registered_user_data(self, register_api, get_user):
        register_api.register(get_user)
        register_api.assert_status_code_is(200)
        register_api.assert_registered_user(get_user)

    @allure.title("Регистрация уже существующего пользователя")
    def test_register_exist_user(self, register_api, default_user):
        register_api.register(default_user)
        register_api.assert_status_code_is(403)
        register_api.assert_response_message("User already exists")

    @allure.title("Регистрация без почти")
    def test_register_without_email(self, register_api, get_user):
        get_user.email = ""
        register_api.register(get_user)
        register_api.assert_status_code_is(403)
        register_api.assert_response_message("Email, password and name are required fields")

    @allure.title("Регистрация без пароля")
    def test_register_without_password(self, register_api, get_user):
        get_user.password = ""
        register_api.register(get_user)
        register_api.assert_status_code_is(403)
        register_api.assert_response_message("Email, password and name are required fields")

    @allure.title("Регистрация без имени")
    def test_register_without_name(self, register_api, get_user):
        get_user.name = ""
        register_api.register(get_user)
        register_api.assert_status_code_is(403)
        register_api.assert_response_message("Email, password and name are required fields")
