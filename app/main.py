from fastapi import FastAPI
from app.adapter.controller.order_controller import order_router as order_controller

app = FastAPI(debug=True)

app.include_router(order_controller)