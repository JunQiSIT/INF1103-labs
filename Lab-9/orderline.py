from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self) -> float:
        return self.product._price * self.quantity
