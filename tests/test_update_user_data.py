import allure

class TestUpdateUserData:

    @allure.title("Изменить данные пользователя с авторизацей")
    def test_update_user_data(self, login_user, update_user_api):
        new_name = "test_name"
        login_user.name = new_name
        update_user_api.update_user(login_user)
        update_user_api.assert_status_code_is(200)
        update_user_api.assert_user_name(new_name)

    @allure.title("Изменить данные пользователя без авторизации")
    def test_update_user_name_without_auth(self, update_user_api, get_user):
        get_user.name = "test_name"
        update_user_api.update_user(get_user)
        update_user_api.assert_status_code_is(401)
