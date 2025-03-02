from sqlalchemy.orm import Session
from app.core.repository.order_repository import OrderRepository
from app.core.model.order import Order
from app.infra.db.database import Base, SessionLocal, engine

from sqlalchemy import Column, Integer, String, Float, DateTime

class OrderDB(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True)
    total_price = Column(Float)

Base.metadata.create_all(bind=engine)

class OrderRepositoryDB(OrderRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def save(self, order: Order):
        order_db = OrderDB(
            id=order.id,
            customer_name=order.customer_name,
            total_price=order.total_price
        )
        self.db_session.add(order_db)
        self.db_session.commit()
        self.db_session.refresh(order_db)
        return order
    
    def get_by_id(self, order_id: int):
        order_db = self.db_session.query(OrderDB).filter(OrderDB.id == order_id).first()
        if order_db:
            return Order(
                id=order_db.id,
                customer_name=order_db.customer_name,
                total_price=order_db.total_price,
            )
        return None
    