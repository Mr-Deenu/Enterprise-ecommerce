from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.core.auth import verify_token

security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    payload = verify_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return payload


def admin_required(current_user=Depends(get_current_user)):
    if not current_user.get("is_admin", False):
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )
    return current_user