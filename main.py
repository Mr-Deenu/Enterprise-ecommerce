from fastapi import FastAPI

from src.database.database import engine
from src.models.user import User
from src.database.database import Base
from src.api.auth import router as auth_router
from src.api.product import router as product_router
from src.models.product import Product
from src.models.order import Order
from src.api.order import router as order_router


Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Enterprise E-Commerce API",
    description="""
Enterprise E-Commerce Backend

Features:
- JWT Authentication
- Product Management
- Order Management
- Admin Authorization
- Pagination
- Product Search
    """,
    version="1.0.0"
)

app.include_router(product_router)
app.include_router(auth_router)
app.include_router(order_router)

@app.get("/")
def home():
    return {
        "message": "Enterprise E-Commerce API Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


