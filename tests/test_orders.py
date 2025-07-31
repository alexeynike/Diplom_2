import allure

class TestOrders:

    @allure.title("Создание нового заказа")
    def test_make_order(self, order_api, login_user, get_burger_ingredients):
        order_api.make_order(get_burger_ingredients)
        order_api.assert_status_code_is(200)
        order_api.assert_success_status()

    @allure.title("Создание заказа не авторизованным пользователем")
    def test_make_order_without_auth(self, order_api, get_burger_ingredients):
        order_api.make_order(get_burger_ingredients)
        order_api.assert_status_code_is(200)
        order_api.assert_success_status()

    @allure.title("Создание заказа с пустым списком ингридиентов")
    def test_make_test_with_empty_ingredients(self, order_api, login_user, get_burger_ingredients):
        get_burger_ingredients["ingredients"] = []
        order_api.make_order(get_burger_ingredients)
        order_api.assert_status_code_is(400)
        order_api.assert_success_status(False)

    @allure.title("Создание заказа с некорректным айди ингридиента")
    def test_make_test_with_wrong_ingredient_id(self, order_api, login_user, get_burger_ingredients):
        get_burger_ingredients["ingredients"][0] = "test_id"
        order_api.make_order(get_burger_ingredients)
        order_api.assert_status_code_is(500)

    @allure.title("Получение заказов пользователя")
    def test_get_user_orders(self, login_user, order_api, make_default_order):
        order_api.get_user_orders()
        order_api.assert_status_code_is(200)
        order_api.assert_success_status()

    @allure.title("Получение заказов не авторизованным юзером")
    def test_get_user_orders_without_auth(self, order_api, make_default_order):
        order_api.get_user_orders()
        order_api.assert_status_code_is(401)
        order_api.assert_success_status(False)
        order_api.assert_response_message("You should be authorised")
