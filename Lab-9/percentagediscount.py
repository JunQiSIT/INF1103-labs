from discountstrategy import DiscountStrategy

class PercentageDiscount(DiscountStrategy):
    def __init__(self, discount_rate: float):
        self._discount_rate = discount_rate

    def apply(self, total: float) -> float:
        return total * (1 - self._discount_rate)
