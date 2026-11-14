from DiscountStrategy import DiscountStrategy

class BulkDiscount(DiscountStrategy):

    def __init__(self, threshold: float, amount: float):
        super().__init__()
        self.__threshold: float = threshold
        self.__amount: float = amount

    def apply(self, total: float) -> float:

        if total >= self.__threshold:
            total -= self.__amount

        return total
