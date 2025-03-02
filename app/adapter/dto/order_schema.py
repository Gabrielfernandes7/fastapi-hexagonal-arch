from pydantic import BaseModel

class OrderSchema(BaseModel):
    id: int
    customer_name: str
    total_price: float