original_count = 0
error_count = 0

while True:
    stock_quantity = input("Please input the stock quantity (input 'quit' to exit the program): ")
    if stock_quantity == "quit":
        print("The current stock count is:", original_count)
        print("The final Failed/Rejected entries count:", error_count)
        break

    
    if stock_quantity.isdigit():
        original_count += int(stock_quantity)
        if original_count > 500:
            print("The final count for the inventory exceeds the limit of 500 units ")
            break
    else:
        try:
            error_count += 1
            if int(stock_quantity) < 0:
                print("The input quantity should not be negative.")
        except:
            print("Please input a integer.")