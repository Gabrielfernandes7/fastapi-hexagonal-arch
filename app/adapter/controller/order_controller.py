from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.adapter.dto.order_schema import OrderSchema
from app.core.model.order import Order
from app.core.service.order_service import OrderService
from app.infra.repository_concrete.order_repository_concrete import OrderRepositoryDB

from app.infra.db.database import SessionLocal

order_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@order_router.post("/orders/")
def create_order(order_data: OrderSchema, db: Session = Depends(get_db)):
    repository = OrderRepositoryDB(db)
    service = OrderService(repository)
    order = Order(**order_data.dict())
    return service.create_order(order)

@order_router.get("/orders/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    repository = OrderRepositoryDB(db)
    service = OrderService(repository)
    return service.get_order(order_id)