from fastapi import APIRouter
from pydantic import BaseModel

from backend.config.security import (
    create_access_token,
    hash_password,
    verify_password
)

router = APIRouter(
    tags=["Authentication"]
)


# ==========================
# Demo User
# ==========================

ADMIN_USERNAME = "admin"

ADMIN_PASSWORD_HASH = hash_password("admin123")


# ==========================
# Request Model
# ==========================

class LoginRequest(BaseModel):

    username: str
    password: str


# ==========================
# Login API
# ==========================

@router.post("/login")
async def login(data: LoginRequest):

    if (
        data.username == ADMIN_USERNAME
        and
        verify_password(
            data.password,
            ADMIN_PASSWORD_HASH
        )
    ):

        token = create_access_token(

            {

                "sub": data.username

            }

        )

        return {

            "status": "success",

            "access_token": token,

            "token_type": "bearer"

        }

    return {

        "status": "failed",

        "message": "Invalid Username or Password"

    }