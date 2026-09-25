max_cap = 500


def process_deliver(current_total, new_value):
    current_total += new_value

    if current_total < max_cap:
        return current_total
    else:
        print("The final count for the inventory exceeds the limit of 500 units")
        return "limit_reach"

def calculate_tax(amount):
    return amount*0.1

def generate_report(total_unit, failed_attempts):
    deliver_tax = calculate_tax(total_unit)

    print("The number of deliveries processes:", total_unit)
    print("The delivery tax:", f"{deliver_tax:.1f}")
    print("The final Failed/Rejected entries count:", failed_attempts)


def get_valid_input():
    product_name = input("\nPlease add in a product name (input 'quit' to exit the program): ")
    
    if product_name.lower() == "quit":
        return "quit"
    else:
        user_input = input("Please input the stock quantity: ")
        if user_input.isdigit():
            return [product_name, int(user_input)]
        else:
            try:
                if int(user_input) < 0:
                    print("The input quantity should not be negative.")
            except:
                print("Please input a integer.")

            return "error"

def load_inventory():
    with open("inventory.txt", "r") as f:
        read_file = f.read()

        split_inventory = []
        if read_file != "":

            split_inventory = read_file.split("\n")
            for i in range(0, len(split_inventory)):
                tmp = split_inventory[i].split(", ")
                split_inventory[i] = tmp

    return split_inventory

def save_inventory(inventory,transaction_history):
    product_id = 1
    if transaction_history != []:
        product_id = int(transaction_history[-1][0]) + 1
    
    inventory[-1] = str(inventory[-1])
    inventory.insert(0, str(product_id))
    
    transaction_history.append(inventory)

    for inven in range(0,len(transaction_history)):
        transaction_history[inven] = ", ".join(transaction_history[inven])
   
    joined_history = "\n".join(transaction_history)
    with open("inventory.txt", "w") as f:
        
        f.write(joined_history)

    print("\nNew Order Added:")
    print(", ".join(inventory))
    print("\nOrder succeddfully saved to inventory.txt")

    

def main():
    error_count = 0
    inventory = 0
    
    while True:
        stocks = load_inventory()
        print("Current Orders:\n")
        for stock in stocks:
            print(", ".join(stock))

        user_input = get_valid_input()

        if user_input == "quit":
            generate_report(inventory,error_count)
            break

        if user_input == "error":
            error_count += 1 
            continue

        
        inventory = process_deliver(inventory,user_input[1])

        if inventory == "limit_reach":
            break

        save_inventory(user_input,stocks)

            
if __name__ == "__main__":
    main()