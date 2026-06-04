from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.services.order_service import get_user_orders
from src.database.database import get_db
from src.schemas.order import OrderCreate
from src.services.order_service import create_order
from src.core.dependencies import get_current_user

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post("/")
def place_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return create_order(
        db,
        current_user["user_id"],
        order.product_id,
        order.quantity
    )

@router.get("/my-orders")
def my_orders(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_user_orders(
        db,
        current_user["user_id"]
    )

@router.get("/history")
def order_history(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return (
        db.query(Order)
        .filter(Order.user_id == current_user["user_id"])
        .all()
    )