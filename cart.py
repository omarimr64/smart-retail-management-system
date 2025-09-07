class Cart:
    __products = []

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
