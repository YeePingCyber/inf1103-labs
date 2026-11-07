from Product import Product
from CanBeShipped import CanBeShipped
from Supplier import Supplier

# Physical Product Class
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight: float, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        print(f"ID: {self.get_product_id()} | Name: {self.get_name()} | Price: ${self.get_price():.2f} | Stock: {self.get_stock()} | Weight: {self.__weight}")

    def get_fulfilment_info(self):
        return "Requires physical shipping."

    def calculate_shipping_cost(self):
        shipping_cost = self.get_price()*0.1
        return shipping_cost
    