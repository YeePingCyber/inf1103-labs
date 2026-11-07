from OrderLine import OrderLine
from Product import Product
class Order:
    def __init__(self, order_id: str):
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def get_order_id(self):
        return self.__order_id
    
    def get_order_lines(self):
        return self.__order_lines
    
    def add_order_line(self, product: Product, quantity: int):
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def calculate_total(self):
        total = 0
        for order_line in self.__order_lines:
            total += order_line.calculate_subtotal()