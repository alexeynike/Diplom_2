import allure


class TestLogin:

    @allure.title("Авторизация существующего пользователя")
    def test_login_exist_user(self, login_api, registered_user):
        login_api.login(registered_user)
        login_api.assert_status_code_is(200)
        login_api.assert_access_token()
        login_api.assert_refresh_token()

    @allure.title("Авторизация с неверным логином")
    def test_with_wrong_login(self, login_api, registered_user):
        registered_user.email = "test.test.123@test.test"
        login_api.login(registered_user)
        login_api.assert_status_code_is(401)

    @allure.title("Авторизация с неверным паролем")
    def test_with_wrong_password(self, login_api, registered_user):
        registered_user.password = "qwerty"
        login_api.login(registered_user)
        login_api.assert_status_code_is(401)
