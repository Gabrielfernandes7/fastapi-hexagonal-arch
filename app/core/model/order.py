# model independente de framework
class Order:
    def __init__(self, id: int, total_price: float, customer_name: str):
        self.id = id
        self.total_price = total_price
        self.customer_name = customer_name
        