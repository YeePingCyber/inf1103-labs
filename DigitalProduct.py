from Product import Product
from Supplier import Supplier

# Digital Product Class
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size: float, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size

    def get_download_size(self):
        return self.__download_size
    
    def display_information(self):
        print(f"ID: {self.get_product_id()} | Name: {self.get_name()} | Price: ${self.get_price():.2f} | Stock: {self.get_stock()} | Download Size: {self.__download_size}")

    def get_fulfilment_info(self):
        return "Requires delivered digitally"