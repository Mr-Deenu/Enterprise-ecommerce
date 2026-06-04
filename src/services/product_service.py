from src.models.product import Product
from sqlalchemy import or_

def create_product(db, product_data):
    product = Product(**product_data.dict())

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def search_products(db, keyword: str):
    return db.query(Product).filter(
        or_(
            Product.name.ilike(f"%{keyword}%"),
            Product.description.ilike(f"%{keyword}%")
        )
    ).all()

def get_products(db):
    return db.query(Product).all()

def get_product_by_id(db, product_id):
    return db.query(Product).filter(
        Product.id == product_id
    ).first()

def update_product(db, product_id, product_data):
    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        return None

    product.name = product_data.name
    product.description = product_data.description
    product.price = product_data.price
    product.stock = product_data.stock

    db.commit()
    db.refresh(product)

    return product

def delete_product(db, product_id):
    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        return False

    db.delete(product)
    db.commit()

    return True

def get_products(
    db,
    search=None,
    skip=0,
    limit=10
):
    query = db.query(Product)

    if search:
        query = query.filter(
            Product.name.contains(search)
        )

    return query.offset(skip).limit(limit).all()


def get_products_paginated(
    db,
    skip: int = 0,
    limit: int = 10
):
    return db.query(Product)\
        .offset(skip)\
        .limit(limit)\
        .all()

def search_products(db, keyword):
    return db.query(Product).filter(
        or_(
            Product.name.ilike(f"%{keyword}%"),
            Product.description.ilike(f"%{keyword}%")
        )
    ).all()