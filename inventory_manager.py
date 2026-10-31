import json
from abc import ABC, abstractmethod

inventory_file = "inventory.json"

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
    def get_fulfilment_info(self) -> str:
        pass

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
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
    
# Inventory Class
class Inventory():
    def __init__(self):
        self.__product_list: list[PhysicalProduct|DigitalProduct] = []

    # Add Product class into the list
    def add_product(self, product: PhysicalProduct|DigitalProduct):
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

# Main Class
class Main():
    def __init__(self):
        self.__file_handling = FileHandling()
        self.__load_inventory = self.__file_handling.loads_inventory()

    def menu(self):
        print("================================")
        print("INVENTORY MANAGEMENT SYSTEM")
        print("================================")
        print("\n--------MENU-----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("-----------------------")

    def __check_float_type(self, user_input):
        try:
            user_input = float(user_input)

            if user_input > 0:
                return True

            return -1
        except:
            return False

    # Get user input
    def get_user_input(self):
        option = input("\nEnter option: ")

        if option.isdigit():
            if int(option) > 6:
                print("Please follow the options given in the menu.")
                return False
            
        else:
            print("Please input the correct option.")
            return False

        # Show all Inventory
        if option == "1":
            self.__load_inventory.display_all()
            return False

        # Add new product
        if option == "2":
            print("\nAdd New Product")
            while True:
                print("\nPlease indicate Physical Product or Digital Product: ")
                print("1. Physical Product")
                print("2. Digital Product")
                product_category_option = input("Please input the options (1 or 2): ")

                if product_category_option == "1":
                    product_category = "physical"
                    break

                if product_category_option == "2":
                    product_category = "digital"
                    break

                print("Please input the options given")

            product_id = input("Product ID: ")
            product_name = input("Product Name: ")

            if product_category == "physical":
                while True:
                    product_weight = input("Product Weight: ")

                    if self.__check_float_type(product_weight) == 1:
                        product_weight = float(product_weight)
                        break

                    if self.__check_float_type(product_weight) == -1:
                        print("Product weight needs to be more than 0.")

                    if self.__check_float_type(product_weight) == 0:
                        print("Please input a valid product weight.")


            if product_category == "digital":
                while True:
                    product_download_size = input("Product Download Size: ")

                    if self.__check_float_type(product_download_size) == 1:
                        product_download_size = float(product_download_size)
                        break

                    if self.__check_float_type(product_download_size) == -1:
                        print("Product download size needs to be more than 0.")

                    if self.__check_float_type(product_download_size) == 0:
                        print("Please input a valid product download size.")

            while True:
                price = input("Price: ")

                try:
                    price = float(price)
                    
                    if price > 0.0:
                        break

                    if price == 0.0:
                        print("Price cannot be 0")
                        continue

                    print("Price cannot be negative")
                except:
                    print("Please enter a valid price")

            while True:
                stock = input("Stock Quantity: ")

                try:
                    stock = int(stock)
                    if stock >= 0:
                        break

                    print("Stock number cannot be negative")
                except:
                    print("Please enter a valid stock number")

            if product_category == "physical":
                product = PhysicalProduct(product_id, product_name, float(price), int(stock), float(product_weight))

            if product_category == "digital":
                product = DigitalProduct(product_id, product_name, float(price), int(stock), float(product_download_size))

            self.__load_inventory.add_product(product)

            print("\nProduct added successfully!")

            return False

        # Update Stock
        if option == "3":
            print("\nUpdate Stock")
            product_id = input("Enter Product ID: ")
            searched_product = self.__load_inventory.search_product(product_id)

            if searched_product:
                new_stock = input("\nNew Stock Quantity: ")
                            
                if new_stock.isdigit():
                    searched_product.update_stock(int(new_stock))
                    print("\nStock updated successfully!")
                else:
                    print("\nPlease input a valid stock value.")

            return False

        # Search product
        if option == "4":
            print("\nSearch Product")
            product_id = input("Enter Product ID: ")
            searched_product = self.__load_inventory.search_product(product_id)

            if searched_product:
                print("\nProduct Found")
                print("-------------------")
                searched_product.display_information()
                print(f"\n{searched_product.get_fulfilment_info()}")

                if isinstance(searched_product, PhysicalProduct):
                    print(f"\nThe shipping cost of this product is {searched_product.calculate_shipping_cost():.2f}")
                print("-------------------")
            else:
                print("\nProduct Not Found")

            return False

        # Save Inventory
        if option == "5":
            self.__file_handling.saves_inventory(self.__load_inventory)

            print("Saving inventory...")
            print("Inventory saved successfully to inventory.json.")
            return False

        # Exit program
        if option == "6":
            self.__file_handling.saves_inventory(self.__load_inventory)
            return True

if __name__ == "__main__":
    is_exit = False
    main_class = Main()

    while not is_exit:
        main_class.menu()
        is_exit = main_class.get_user_input()

    print("Saving inventory before exit...")
    print("Inventory saved successfully.\n")
    print("Thank you for using Inventory Management System.")
    print("Program terminated.")