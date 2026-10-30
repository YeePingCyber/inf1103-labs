import json

inventory_file = "inventory.json"

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