import json

inventory_file = "inventory.json"

# Product Class
class Product():
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
        for product in self.__product_list:
            product.display_information()
        print("----------------------------")


# File Handling Class
class FileHandling():
    def __init__(self):
        self.__inventory = Inventory()
        

    def loads_inventory(self):
        # inventory = []
        try:
            with open(inventory_file, "r") as f:
                inventory_list = json.load(f)
                status = 200
        except:
            status = 404

        if inventory_list and status == 200:
            for inventory in inventory_list:
                product = Product(inventory["id"],inventory["name"],inventory["price"],inventory["stock"])
                self.__inventory.add_product(product)

        return self.__inventory

    def saves_inventory(self, inventory: Inventory):
        product_list = inventory.get_product_list()

        list_product = []
        for product in product_list:
            list_product.append({"id": product.get_product_id(), "name": product.get_name(), "price": product.get_price(), "stock": product.get_stock()})

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
            product_id = input("Product ID: ")
            product_name = input("Product Name: ")

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
            
            product = Product(product_id, product_name, float(price), int(stock))
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
                print("-------------------")
            else:
                print("\nProduct Not Found")

            return False

        # Save Inventory
        if option == "5":
            self.__file_handling.saves_inventory(self.__load_inventory)

            self.__load_inventory.display_all()
            print("Saving inventory...")
            print("Inventory saved successfully to inventory.json.")
            return False

        # Exit program
        if option == "6":
            self.__file_handling.saves_inventory(self.__load_inventory)
            return True



if __name__ == "__main__":
    # main()
    is_exit = False
    main_class = Main()

    while not is_exit:
        main_class.menu()
        is_exit = main_class.get_user_input()

    print("Saving inventory before exit...")
    print("Inventory saved successfully.\n")
    print("Thank you for using Inventory Management System.")
    print("Program terminated.")