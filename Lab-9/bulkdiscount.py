from discountstrategy import DiscountStrategy

class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, discount_rate: float):
        self._threshold = threshold
        self._discount_rate = discount_rate

    def apply(self, total: float) -> float:
        if total >= self._threshold:
            return total * (100 - self._discount_rate) / 100
        return total
