import json


class Product:
    def __init__(self, id, name, price, stock_quantity):
        self.id = id
        self.name = name
        self.stock_quantity = stock_quantity
        self.price = price

    # C
    @classmethod
    def add_product(cls, id, name, price, stock_quantity):
        return cls(id, name, price, stock_quantity)

    # R
    @classmethod
    def get_product(cls, id):
        for p in cls.products:
            if p["id"] == id:
                return p

    # U
    @classmethod
    def buy_product(cls, id, quantity):
        def create_new_products(p):
            if p["id"] == id:

                if p["stock_quantity"] > quantity:
                    p["stock_quantity"] -= quantity
                else:
                    raise ValueError("Not enough quantity")

            return p

        # Updating products
        new_products = list(map(create_new_products, cls.products))
        cls.products = new_products

        # Updating json file
        with open(cls.data_path, "w") as f:
            json.dump(new_products, f, indent=2)

        # returning the new products
        return new_products


class Grocery(Product):
    discount_rule = {"ratio": 0.05, "for_quantity": 250, "max": 0.25}
    products = []
    data_path = "grocery.json"
    name = "grocery"

    def __init__(self, id, name, price, stock_quantity):
        super().__init__(id, name, price, stock_quantity)
        self.discount_rule = Grocery.discount_rule
        Grocery.products.append(self.__dict__)


class Stationary(Product):
    discount_rule = {"ratio": 0.02, "for_quantity": 50, "max": 0.2}
    products = []
    data_path = "stationary.json"
    name = "stationary"

    def __init__(self, id, name, price, stock_quantity):
        super().__init__(id, name, price, stock_quantity)
        self.discount_rule = Stationary.discount_rule
        Stationary.products.append(self.__dict__)


# Adding grocery products
with open(Grocery.data_path, "r") as g:
    g_products = json.load(g)
    for p in g_products:
        Grocery.add_product(p["id"], p["name"], p["price"], p["stock_quantity"])

# Adding stationary products
with open(Stationary.data_path, "r") as s:
    s_products = json.load(s)
    for p in s_products:
        Stationary.add_product(p["id"], p["name"], p["price"], p["stock_quantity"])
