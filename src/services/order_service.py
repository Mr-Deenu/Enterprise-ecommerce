from src.models.order import Order
from src.models.product import Product

def create_order(
    db,
    user_id,
    product_id,
    quantity
):
    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        return {"message": "Product not found"}

    total_price = product.price * quantity

    order = Order(
        user_id=user_id,
        product_id=product_id,
        quantity=quantity,
        total_price=total_price
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return order

def get_user_orders(
    db,
    user_id
):
    return db.query(Order).filter(
        Order.user_id == user_id
    ).all()

def get_user_orders(db, user_id):
    return db.query(Order).filter(
        Order.user_id == user_id
    ).all()