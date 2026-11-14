from PercentageDiscount import PercentageDiscount

class StudentDiscount(PercentageDiscount):
    def __init__(self, percentage):
        super().__init__(percentage)