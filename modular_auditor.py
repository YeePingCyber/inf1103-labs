max_cap = 500
tax_rate = 0.1

def process_deliver(current_total, new_value):
    current_total += new_value

    if current_total < max_cap:
        return current_total
    else:
        print("The final count for the inventory exceeds the limit of 500 units")
        return "limit_reach"

def calculate_tax(amount):
    return amount*tax_rate

def generate_report(total_unit, failed_attempts):
    deliver_tax = calculate_tax(total_unit)

    print("The number of deliveries processes:", total_unit)
    print("The delivery tax:", deliver_tax)
    print("The final Failed/Rejected entries count:", failed_attempts)

def get_valid_input():
    user_input = input("Please input the stock quantity (input 'quit' to exit the program): ")

    if user_input.lower() == "quit":
        return "quit"
    else:
        if user_input.isdigit():
            return int(user_input)
        else:
            try:
                if int(user_input) < 0:
                    print("The input quantity should not be negative.")
            except:
                print("Please input a integer.")

            return "error"

def main():
    inventory = 0
    error_count = 0

    while True:
        user_input = get_valid_input()
        if user_input == "quit":
            generate_report(inventory,error_count)
            break

        if user_input == "error":
            error_count += 1 
            continue

        inventory = process_deliver(inventory,user_input)

        if inventory == "limit_reach":
            break
            
if __name__ == "__main__":
    main()