from PercentageDiscount import PercentageDiscount

class StudentDiscount(PercentageDiscount):
    def __init__(self, percentage: float):
        super().__init__(percentage)