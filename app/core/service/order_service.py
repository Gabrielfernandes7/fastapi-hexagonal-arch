from app.core.model.order import Order
from app.core.repository.order_repository import OrderRepository

class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def create_order(self, order: Order):
        return self.repository.save(order)
    
    def get_order(self, order_id: int):
        return self.repository.get_by_id(order_id)
