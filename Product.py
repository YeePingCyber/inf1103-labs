from CanBeShipped import CanBeShipped
from abc import ABC, abstractmethod
# Product Class
class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_stock(self):
        return self.__stock
    
    def update_stock(self, quantity: int):
        self.__stock = quantity

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")

    @abstractmethod
    def get_fulfilment_info(self):
        pass

# Physical Product Class
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight: float):
        super().__init__(product_id, name, price, stock)
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

# Digital Product Class
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size: float):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def get_download_size(self):
        return self.__download_size
    
    def display_information(self):
        print(f"ID: {self.get_product_id()} | Name: {self.get_name()} | Price: ${self.get_price():.2f} | Stock: {self.get_stock()} | Download Size: {self.__download_size}")

    def get_fulfilment_info(self):
        return "Requires delivered digitally"
