from OrderLine import OrderLine
from Product import Product
from DiscountStrategy import DiscountStrategy

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy):
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []
        self.__discount: DiscountStrategy = discount

    def get_order_id(self) -> str:
        return self.__order_id
    
    def get_order_lines(self) -> list[OrderLine]:
        return self.__order_lines

    def remove_order_lines(self, index: int) -> None:
        deleted_order = self.__order_lines.pop(index)
        print(f"{deleted_order.get_product().get_name()} order is being removed")

    def display_order_lines(self) -> None:
        for orderline in self.__order_lines:
            print(f"Name: {orderline.get_product().get_name()} | Quantity: {orderline.get_quantity()} | Subtotal: {orderline.calculate_subtotal()}")

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0.0
        for order_line in self.__order_lines:
            total += order_line.calculate_subtotal()

        return self.__discount.apply(total)

    def set_discount(self, discount: DiscountStrategy):
        self.__discount = discount