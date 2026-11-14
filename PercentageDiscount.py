from DiscountStrategy import DiscountStrategy

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        super().__init__()
        self.__percentage: float = percentage

    def apply(self, total: float) -> float:
        percent = (100-self.__percentage)/100
        discounted_value = total * percent
        return discounted_value