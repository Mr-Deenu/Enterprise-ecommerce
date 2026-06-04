from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.schemas.user import UserLogin
from src.services.user_service import authenticate_user
from src.core.auth import create_access_token
from src.schemas.user import UserCreate
from src.database.database import get_db
from src.services.user_service import create_user
from src.core.dependencies import get_current_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(
        db,
        user.username,
        user.email,
        user.password
    )

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = authenticate_user(
        db,
        user.email,
        user.password
    )

    if not db_user:
        return {"message": "Invalid credentials"}

    token = create_access_token(
        {
            "sub": db_user.email,
            "user_id": db_user.id,
            "is_admin": db_user.is_admin
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }




@router.get("/me")
def me(current_user=Depends(get_current_user)):
    return {
        "user": current_user
    }


@router.post(
    "/register",
    summary="Register User",
    description="Create a new user account"
)
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(
        db,
        user.username,
        user.email,
        user.password
    )

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }

@router.post(
    "/login",
    summary="Login User",
    description="Generate JWT token"
)
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = authenticate_user(
        db,
        user.email,
        user.password
    )

    if not db_user:
        return {"message": "Invalid credentials"}

    token = create_access_token(
        {
            "sub": db_user.email,
            "user_id": db_user.id,
            "is_admin": db_user.is_admin
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }