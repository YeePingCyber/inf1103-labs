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
    
    def update_stock(self, quantity: int):
        self.__stock = quantity

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")

# Inventory Class
class Inventory():
    def __init__(self):
        self.__product_list: list[Product]

    # Add Product class into the list
    def add_product(self, product: Product):
        self.__product_list.append(product)

    # Search product by ID
    def search_product(self, id):
        product_found = False
        for product in self.__product_list:
            if product.get_product_id() == id:
                print("Product Found")
                print("----------------------------")
                product.display_information()
                print("----------------------------")
                product_found = True
                break

        if not product_found:
            print("\nProduct Not Found")
        
    # Display all product
    def display_all(self):
        print("Current Inventory")
        print("----------------------------")
        for product in self.__product_list:
            product.display_information()
        print("----------------------------")

def load_inventory():
    inventory = []
    try:
        with open(inventory_file, "r") as f:
            inventory = json.load(f)
            status = 200
    except:
        status = 404

    
    return inventory, status

def save_inventory(inventory):

    with open(inventory_file, "w") as f:
        json.dump(inventory, f, indent=4)
    

def search_product(inventory, product_id):
    product_found = False
    for i in inventory:
        if i["id"] == product_id:
            print("\nProduct Found")
            print("-------------------")
            print(f"ID: {i["id"]}")
            print(f"Name: {i["name"]}")
            print(f"Price: {i["price"]}")
            print(f"Stock: {i["stock"]}")
            print("-------------------")
            product_found = True
            break

    if not product_found:
        print("\nProduct Not Found")
        return

def add_product(inventory, product_id, name, price, stock):
    product = {"id":product_id, "name":name, "price":float(price), "stock":int(stock)}
    inventory.append(product)
    print("\nProduct added successfully!")
    return

def update_stock(inventory, product_id):
    product_found = False
    for i in range(0,len(inventory)):
        if inventory[i]["id"] == product_id:
            print("\nProduct Found")
            print(f"Name: {inventory[i]["name"]}")
            print(f"Current Stock: {inventory[i]["stock"]}")
            product_found = True

            new_stock = input("\nNew Stock Quantity: ")
            
            if new_stock.isdigit():
                inventory[i]["stock"] = int(new_stock)
                print("\nStock updated successfully!")
                return inventory
            else:
                print("\nPlease input a valid stock value.")
            break
    
    if not product_found:
        print("\nProduct Not Found")
        return

    

    

    

def display_all(inventory):
    print("\nCurrent Inventory")
    print("-------------------------")
    if inventory == []:
        print("The inventory is currently empty.")
    else:
        for i in inventory:
            print(f"ID: {i["id"]} | Name: {i["name"]} | Price: ${i["price"]:.2f} | Stock: {i["stock"]}")
    print("-------------------------")


    return

def menu():
    print("\n--------MENU-----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("-----------------------")

    option = input("\nEnter option: ")

    if option.isdigit():
        if int(option) > 6:
            print("Please follow the options given in the menu.")
            return False
        else:
            return option
    else:
        print("Please input the correct option.")
        return False


def main():
    print("================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("================================")

    inventory, status = load_inventory()
    
    print("\ninventory.json found.")
    print("inventory loaded successfully.")

    while True:
        user_input = menu()

        # Show all Inventory
        if user_input == "1":
            display_all(inventory)

        # Add new product
        if user_input == "2":
            print("\nAdd New Product")
            product_id = input("Product ID: ")
            product_name = input("Product Name: ")
            price = input("Price: ")
            stock = input("Stock Quantity: ")
            add_product(inventory, product_id, product_name, price, stock)

        # Update Stock
        if user_input == "3":
            print("\nUpdate Stock")
            product_id = input("Enter Product ID: ")
            inventory = update_stock(inventory, product_id)

        # Search product
        if user_input == "4":
            print("\nSearch Product")
            product_id = input("Enter Product ID: ")
            search_product(inventory, product_id)

        # Save Inventory
        if user_input == "5":
            save_inventory(inventory)
            print("Saving inventory...")
            print("Inventory saved successfully to inventory.json.")

        # Exit program
        if user_input == "6":
            save_inventory(inventory)
            break

    print("Saving inventory before exit...")
    print("Inventory saved successfully.\n")
    print("Thank you for using Inventory Management System.")
    print("Program terminated.")



if __name__ == "__main__":
    main()