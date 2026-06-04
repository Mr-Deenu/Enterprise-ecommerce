from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.database.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    product_id = Column(Integer, ForeignKey("products.id"))

    quantity = Column(Integer, nullable=False)

    total_price = Column(Float, nullable=False)

    status = Column(String(50), default="Pending")