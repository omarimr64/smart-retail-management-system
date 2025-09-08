import json


class Cart:
    __products = []
    __total_cart_price = 0
    __currency_data = {}

    @classmethod
    def add_product(cls, product_class, product, quantity):
        cls.__products.append(
            {"product": product, "store": product_class, "quantity": quantity}
        )

    @classmethod
    def get_products(cls):
        return cls.__products

    @classmethod
    def clear(cls):
        cls.__products = []
        cls.__total_cart_price = 0

    @classmethod
    def get_final_price(cls, p):
        first_price = p["quantity"] * p["product"]["price"]
        for_quantity = p["product"]["discount_rule"]["for_quantity"]
        discount_multiply = int(p["quantity"] / for_quantity)
        discount = discount_multiply * p["product"]["discount_rule"]["ratio"]

        if discount > p["product"]["discount_rule"]["max"]:
            discount = p["product"]["discount_rule"]["max"]

        last_price = first_price * (1 - discount)
        cls.__total_cart_price += last_price

        return "{:.2f}".format(last_price)

    @classmethod
    def get_total_price(cls, currency):
        tp = cls.__total_cart_price * cls.__currency_data[currency]
        return "{:.2f}".format(tp)

    @classmethod
    def get_currencies(cls):
        # Adding currencies
        with open("currencies.json", "r") as c:
            currencies = json.load(c)
            cls.__currency_data = currencies[0]

        # Returning currency options
        currency_options = list(cls.__currency_data.keys())
        return currency_options


# I want to know how much there is 250 kg and what is the discount and check the maximum
