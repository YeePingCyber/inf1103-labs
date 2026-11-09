from Product import Product
from Supplier import Supplier

# Digital Product Class
class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size: float = download_size

    def get_download_size(self) -> float:
        return self.__download_size
    
    def display_information(self) -> None:
        print(f"ID: {self.get_product_id()} | Name: {self.get_name()} | Price: ${self.get_price():.2f} | Stock: {self.get_stock()} | Download Size: {self.__download_size}")

    def get_fulfilment_info(self) -> str:
        return "Requires delivered digitally"