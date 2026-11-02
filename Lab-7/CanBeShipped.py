from abc import ABC, abstractmethod

# Base abstract class for shipping
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass