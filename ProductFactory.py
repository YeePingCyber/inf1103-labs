from Supplier import Supplier
from Product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float, stock_quantity: int, extra_value: float, supplier: Supplier) -> Product:
        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock_quantity, extra_value, supplier)
        elif product_type == "digital":
            return DigitalProduct(product_id, name, price, stock_quantity, extra_value, supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")