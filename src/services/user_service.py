from sqlalchemy.orm import Session
from src.models.user import User
from src.core.security import hash_password

from src.core.security import verify_password



def create_user(db: Session, username, email, password):
    existing_user = db.query(User).filter(
        User.email == email
    ).first()

    if existing_user:
        raise ValueError("Email already registered")
    user = User(
        username=username,
        email=email,
        hashed_password=hash_password(password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


from src.models.user import User

def authenticate_user(db, email, password):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user