from FileHandling import FileHandling
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier
from Inventory import Inventory
from Order import Order
from NoDiscount import NoDiscount
from PercentageDiscount import PercentageDiscount
from BulkDiscount import BulkDiscount
from StudentDiscount import StudentDiscount
from ProductFactory import ProductFactory

import csv

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

    def __get_positive_float(self, prompt: str) -> float:
        while True:
            try:
                value = float(input(prompt))

                if value <= 0:
                    print("Please enter a number greater than zero.")
                    continue

                return value
            except ValueError:
                print("Please enter a valid number, e.g. 12.50")

    def __get_positive_int(self, prompt: str) -> int:
        while True:
            try:
                value = int(input(prompt))

                if value <= 0:
                    print("Please enter a number greater than zero.")
                    continue

                return value
            except ValueError:
                print("Please enter a valid number, e.g. 12")

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
                extra_value = self.__get_positive_float("Product Weight: ")

            if product_category == "digital":
                extra_value = self.__get_positive_float("Product Download Size: ")


            price = self.__get_positive_float("Price: ")

            stock = self.__get_positive_int("Stock Quantity: ")


            supplier_id = input("Supplier ID: ")
            supplier_name = input("Supplier name: ")
            contact_email = input("Contact Email: ")

            supplier = Supplier(supplier_id, supplier_name, contact_email)

            product = ProductFactory.create(product_category, product_id, product_name, price, stock, extra_value, supplier)

            self.__load_inventory.add_product(product)

            print("\nProduct added successfully!")

            return False

        # Update Stock
        if option == "3":
            print("\nUpdate Stock")
            product_id = input("Enter Product ID: ")
            searched_product = self.__load_inventory.search_product(product_id)

            if searched_product:
                new_stock = self.__get_positive_int("\nNew Stock Quantity: ")
                searched_product.update_stock(new_stock)

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

            order = Order(order_id, NoDiscount())
            while add_more:
                product_id = input("Product ID: ")

                searched_product = self.__load_inventory.search_product(product_id)
                
                if searched_product:
                    quantity = self.__get_positive_int("Quantity: ")
                    order.add_order_line(searched_product, quantity)

                    print("\nOrder added successfully.")
                else:
                    print("\nProduct Not Found")

                is_continue = input("Do you want to buy more products. (Y/N): ")

                if is_continue.lower() == "n":
                    add_more = False

            # Get discount
            while True:
                print("Select the discount")
                print("1. Bulk Discount")
                print("2. Percent Discount")
                print("3. Student Discount")
                print("4. No Discount")

                discount_option = input("Discount option: ")

                if discount_option == "1":
                    order.set_discount(BulkDiscount(200,20))
                    print("Bulk discount has been applied")
                    break

                if discount_option == "2":
                    percentage = self.__get_positive_float("Please input a percentage")
                    order.set_discount(PercentageDiscount(percentage))
                    print(f"{percentage}% discount has been applied")
                    break

                if discount_option == "3":
                    order.set_discount(StudentDiscount(5))
                    print("Student discount has been applied")
                    break

                if discount_option == "4":
                    print("No discount applied")
                    break

                print("Please input the options given in the menu")


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

    def load_product(self, path: str, inventory: Inventory, supplier: Supplier) -> None:
        loaded = 0
        try:
            file = open(path, newline="")
        except FileNotFoundError:
            print(f"Products file not found: {path}")
        else:
            with file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    try:
                        product = ProductFactory.create(row[0], row[1], row[2], row[3], row[4], 25.0, supplier)
                        inventory.add_product(product)
                        loaded += 1
                    except ValueError:
                        print(f"Unknown product type: {row[0]}")
                    continue
            print(f"{loaded} Products loaded")
        finally:
            print("Load attempt finished.")


if __name__ == "__main__":
    is_exit = False
    main_class = Main()

    # while not is_exit:
    #     main_class.menu()
    #     is_exit = main_class.get_user_input()

    # print("Saving inventory before exit...")
    # print("Inventory saved successfully.\n")
    # print("Thank you for using Inventory Management System.")
    # print("Program terminated.")


    # Run only the load product fucntion
    inventory = Inventory()
    supplier = Supplier("S01", "Test", "Test@gmail.com")
    main_class.load_product("products.csv", inventory, supplier)