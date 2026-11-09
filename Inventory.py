from Product import Product
# Inventory Class
class Inventory:
    def __init__(self):
        self.__product_list: list[Product] = []
        self.__deleted_product: list[Product] = []

    # Add Product class into the list
    def add_product(self, product: Product) -> None:
        self.__product_list.append(product)

    # Retrieve Product listing
    def get_product_list(self) -> list[Product]:
        return self.__product_list
    
    def get_deleted_product(self) -> list[Product]:
        return self.__deleted_product
    
    # Search product by ID
    def search_product(self, id) -> Product|None:
        for product in self.__product_list:
            if product.get_product_id() == id:
                return product

    # Remove product
    def remove_product(self, product_id: str) -> None:
        for i in range(len(self.__product_list)):
            if self.__product_list[i].get_product_id() == product_id:
                deleted_product = self.__product_list.pop(i)
                self.__deleted_product.append(deleted_product)
                print(f"{deleted_product.get_name()} has been deleted successfully")
        
    # Display all product
    def display_all(self) -> None:
        print("Current Inventory")
        print("----------------------------")
        if self.__product_list:
            for product in self.__product_list:
                product.display_information()
        else:
            print("Inventory is currently empty")
        print("----------------------------")