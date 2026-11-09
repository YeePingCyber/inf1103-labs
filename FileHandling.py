# File Handling Class
import json
from Inventory import Inventory
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier

# File Handling Class
class FileHandling:
    def __init__(self):
        self.__inventory: Inventory = Inventory()
        self.__inventory_file = "inventory.json"
        self.__supplier_file = "supplier.json"
        self.__deleted_file = "deleted.json"
        

    def loads_inventory(self) -> Inventory:
        inventory_list = []
        supplier_list = []
        try:
            with open(self.__inventory_file, "r") as f:
                inventory_list = json.load(f)
                
        except:
            print("Unable to load inventory file")

        try:
            with open(self.__supplier_file, "r") as f:
                supplier_list = json.load(f)
                
        except:
            print("Unable to load supplier file")

        if inventory_list:
            for inventory in inventory_list:
                for supplier in supplier_list:
                    if inventory["supplier_id"] == supplier["supplier_id"]:
                        supplier = Supplier(supplier["supplier_id"], supplier["name"], supplier["contact_email"])

                        if inventory.get("category") == "physical":
                            product = PhysicalProduct(inventory["id"],inventory["name"],inventory["price"],inventory["stock"],inventory["weight"], supplier)

                        if inventory.get("category") == "digital":
                            product = DigitalProduct(inventory["id"],inventory["name"],inventory["price"],inventory["stock"],inventory["download_size"], supplier)

                        self.__inventory.add_product(product)

        return self.__inventory
    

    def saves_inventory(self, inventory: Inventory) -> None:
        product_list = inventory.get_product_list()
        deleted_list = inventory.get_deleted_product()

        list_product = []
        deleted_product = []
        supplier_list = []

        supplier_id_list = []
        
        for product in product_list:
            supplier = product.get_supplier()
            supplier_id = supplier.get_supplier_id()

            if  supplier_id not in supplier_id_list:
                supplier_dict = {"supplier_id":supplier_id, "name": supplier.get_name(), "contact_email": supplier.get_contact_email()}
                supplier_list.append(supplier_dict)
                supplier_id_list.append(supplier.get_supplier_id())

            if isinstance(product, PhysicalProduct):
                list_product.append({"id": product.get_product_id(), "name": product.get_name(),"category": "physical", "price": product.get_price(), "stock": product.get_stock(), "weight": product.get_weight(), "supplier_id": supplier_id})

            if isinstance(product, DigitalProduct):
                list_product.append({"id": product.get_product_id(), "name": product.get_name(),"category": "digital", "price": product.get_price(), "stock": product.get_stock(), "download_size": product.get_download_size(), "supplier_id": supplier_id})
        
        
        for deleted in deleted_list:

            if isinstance(deleted, PhysicalProduct):
                deleted_product.append({"id": deleted.get_product_id(), "name": deleted.get_name(),"category": "physical", "price": deleted.get_price(), "stock": deleted.get_stock(), "weight": deleted.get_weight(), "supplier_id": supplier_id})

            if isinstance(deleted, DigitalProduct):
                deleted_product.append({"id": deleted.get_product_id(), "name": deleted.get_name(),"category": "digital", "price": deleted.get_price(), "stock": deleted.get_stock(), "download_size": deleted.get_download_size(), "supplier_id": supplier_id})


               
        with open(self.__inventory_file, "w") as f:
            json.dump(list_product, f, indent=4)

        with open(self.__supplier_file, "w") as f:
            json.dump(supplier_list, f, indent=4)

        with open(self.__deleted_file, "w") as f:
            json.dump(deleted_product, f, indent=4)
