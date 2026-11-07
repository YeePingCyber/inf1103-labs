from Product import Product
class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.__product = product
        self.__quantity = quantity

    def get_product(self):
        return self.__product
    
    def get_quantity(self):
        return self.__quantity
    
    def calculate_subtotal(self):
        return self.__product.get_price() * self.__quantity