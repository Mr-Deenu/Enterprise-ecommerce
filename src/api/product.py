from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import Query
from src.schemas.product import ProductCreate

from src.services.product_service import create_product
from src.services.product_service import get_products

from src.services.product_service import search_products
from src.services.product_service import get_product_by_id
from src.services.product_service import update_product

from src.database.database import get_db
from src.core.dependencies import admin_required

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/")
def list_products(
    search: str = Query(None),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return get_products(
        db,
        search,
        skip,
        limit
    )
@router.get("/")
def list_products(
    db: Session = Depends(get_db)
):
    return get_products(db)

@router.get("/search/")
def search_product(
    keyword: str = Query(...),
    db: Session = Depends(get_db)
):
    return search_products(db, keyword)

@router.post("/")
def add_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):
    return create_product(db, product)

@router.get("/{product_id}")
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    return get_product_by_id(
        db,
        product_id
    )


@router.put("/{product_id}")
def update_product_api(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    updated_product = update_product(
        db,
        product_id,
        product
    )

    if not updated_product:
        return {"message": "Product not found"}

    return updated_product

from src.services.product_service import delete_product

@router.delete("/{product_id}")
def delete_product_api(
    product_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_product(
        db,
        product_id
    )

    if not deleted:
        return {"message": "Product not found"}

    return {"message": "Product deleted successfully"}

from src.services.product_service import get_products_paginated

@router.get("/")
def list_products(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return db.query(Product)\
        .offset(skip)\
        .limit(limit)\
        .all()

