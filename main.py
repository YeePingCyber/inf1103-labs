from FileHandling import FileHandling
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier
from Inventory import Inventory
from Order import Order

# Main Class
class Main:
    def __init__(self):
        self.__file_handling: FileHandling = FileHandling()
        self.__load_inventory: Inventory = self.__file_handling.loads_inventory()
        self.__orders: list[Order] = []

    def menu(self) -> None:
        print("================================")
        print("INVENTORY MANAGEMENT SYSTEM")
        print("================================")
        print("\n--------MENU-----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Remove Product")
        print("6. Add Order")
        print("7. Remove Order")
        print("8. Save Inventory")
        print("9. Exit")
        print("-----------------------")

    def __check_float_type(self, user_input) -> bool:
        try:
            user_input = float(user_input)

            if user_input > 0:
                return True

            return -1
        except:
            return False

    # Get user input
    def get_user_input(self) -> bool:
        option = input("\nEnter option: ")

        if option.isdigit():
            if int(option) > 9:
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

            supplier_id = input("Supplier ID: ")
            supplier_name = input("Supplier name: ")
            contact_email = input("Contact Email: ")

            supplier = Supplier(supplier_id, supplier_name, contact_email)
            
            if product_category == "physical":
                product = PhysicalProduct(product_id, product_name, float(price), int(stock), float(product_weight), supplier)

            if product_category == "digital":
                product = DigitalProduct(product_id, product_name, float(price), int(stock), float(product_download_size), supplier)

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
                supplier_info = searched_product.get_supplier()
                print("\nProduct Found")
                print("--------------------------------------")
                searched_product.display_information()
                print(f"\n{searched_product.get_fulfilment_info()}")

                if isinstance(searched_product, PhysicalProduct):
                    print("--------------------------------------")
                    print(f"The shipping cost of this product is {searched_product.calculate_shipping_cost():.2f}")

                print("--------------------------------------")
                supplier_info.display_information()
                print("--------------------------------------")
            else:
                print("\nProduct Not Found")

            return False

        # remove Product
        if option == "5":
            print("\nRemove Product")
            product_id = input("Enter Product ID: ")
            searched_product = self.__load_inventory.search_product(product_id)

            if searched_product:
                confirmation = input("Are you sure you want to remove this product (Y/N): ")

                if confirmation.lower() == "y":
                    self.__load_inventory.remove_product(product_id)
                else:
                    print("The product has not been remove")
            else:
                print("\nProduct Not Found")

            return False
        
        # Add OrderLine
        if option == "6":
            print("Add Order")
            order_id = input("Order ID: ")

            add_more = True

            order = Order(order_id)
            while add_more:
                product_id = input("Product ID: ")

                searched_product = self.__load_inventory.search_product(product_id)
                
                if searched_product:
                    quantity = input("Quantity: ")
                    order.add_order_line(searched_product, int(quantity))

                    print("\nOrder added successfully.")
                else:
                    print("\nProduct Not Found")

                is_continue = input("Do you want to buy more products. (Y/N): ")

                if is_continue.lower() == "n":
                    add_more = False

            # Calculate total
            self.__orders.append(order)
            order.display_order_lines()
            print(f"The total amount: ${order.calculate_total():.2f}")

        # Remove OrderLine
        if option == "7":
            print("Remove Order")
            order_id = input("Order ID: ")
            product_id = input("Product ID: ")
            order_lines = []

            for order in self.__orders:
                if order.get_order_id() == order_id:
                    searched_order = order
                    order_lines = searched_order.get_order_lines()

            for i in range(len(order_lines)):
                if order_lines[i].get_product().get_product_id() == product_id:
                    
                    searched_order.remove_order_lines(i)
                    searched_order.display_order_lines()
                    break

            return False

        # Save Inventory
        if option == "8":
            self.__file_handling.saves_inventory(self.__load_inventory)

            print("Saving inventory...")
            print("Inventory saved successfully to inventory.json.")
            return False

        # Exit program
        if option == "9":
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