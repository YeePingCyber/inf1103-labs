from FileHandling import FileHandling
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier

# Main Class
class Main:
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
        print("5. Remove Product")
        print("6. Add Order")
        print("7. Save Inventory")
        print("8. Exit")
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

            supplier_info = searched_product.get_supplier()

            if searched_product:
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
        
        # Save Inventory
        if option == "6":
            self.__file_handling.saves_inventory(self.__load_inventory)

            print("Saving inventory...")
            print("Inventory saved successfully to inventory.json.")
            return False

        # Exit program
        if option == "7":
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