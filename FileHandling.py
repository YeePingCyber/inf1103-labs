# File Handling Class
import json
from Inventory import Inventory
from Product import PhysicalProduct, DigitalProduct

inventory_file = "inventory.json"

# File Handling Class
class FileHandling():
    def __init__(self):
        self.__inventory = Inventory()
        

    def loads_inventory(self):
        inventory_list = []
        try:
            with open(inventory_file, "r") as f:
                inventory_list = json.load(f)
                status = 200
        except:
            status = 404

        if inventory_list and status == 200:
            for inventory in inventory_list:
                product = ""
                if inventory.get("category") == "physical":
                    product = PhysicalProduct(inventory["id"],inventory["name"],inventory["price"],inventory["stock"],inventory["weight"])

                if inventory.get("category") == "digital":
                    product = DigitalProduct(inventory["id"],inventory["name"],inventory["price"],inventory["stock"],inventory["download_size"])

                self.__inventory.add_product(product)

        return self.__inventory

    def saves_inventory(self, inventory: Inventory):
        product_list = inventory.get_product_list()

        list_product = []
        
        for product in product_list:
            if isinstance(product, PhysicalProduct):
                list_product.append({"id": product.get_product_id(), "name": product.get_name(),"category": "physical", "price": product.get_price(), "stock": product.get_stock(), "weight": product.get_weight()})

            if isinstance(product, DigitalProduct):
                list_product.append({"id": product.get_product_id(), "name": product.get_name(),"category": "digital", "price": product.get_price(), "stock": product.get_stock(), "download_size": product.get_download_size()})

            

        with open(inventory_file, "w") as f:
            json.dump(list_product, f, indent=4)