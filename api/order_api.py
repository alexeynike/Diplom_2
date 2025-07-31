from api.base_api import BaseApi


class OrderApi(BaseApi):
    def make_order(self, ingredients):
        self.post("/orders", body=ingredients)

    def get_user_orders(self):
        self.get("/orders")