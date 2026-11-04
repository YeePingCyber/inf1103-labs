from Product import Product
# Inventory Class
class Inventory():
    def __init__(self):
        self.__product_list: list[Product] = []

    # Add Product class into the list
    def add_product(self, product: Product):
        self.__product_list.append(product)

    # Retrieve Product listing
    def get_product_list(self):
        return self.__product_list
    
    # Search product by ID
    def search_product(self, id):
        for product in self.__product_list:
            if product.get_product_id() == id:
                return product

        return ""
        
    # Display all product
    def display_all(self):
        print("Current Inventory")
        print("----------------------------")
        if self.__product_list:
            for product in self.__product_list:
                product.display_information()
        else:
            print("Inventory is currently empty")
        print("----------------------------")