from discountstrategy import DiscountStrategy


class StudentDiscount(DiscountStrategy):
    def __init__(self, discount_rate: float = 15.0):
        self.discount_rate: float = discount_rate

    def apply(self, total: float) -> float:
        return total * (100 - self.discount_rate) / 100
