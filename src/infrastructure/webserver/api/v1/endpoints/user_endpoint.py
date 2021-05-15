from datetime import datetime, timedelta
from typing import Optional
from fastapi import APIRouter
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from src.interfaces.controllers.user_controller import UserController
from src.interfaces.serializers.user_serializer import UserCustomerIn, UserCustomerOut
from src.domain.entities.users_entity import UserEntity

router = APIRouter(
    prefix="",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)
class HTTPError(BaseModel):
    detail: str
    class Config:
        schema_extra = {
            "example": {"detail": "HTTPException raised."},
        }


@router.post("/customer/create/", response_model=UserCustomerOut, 
    response_model_exclude_unset=True,
    responses={
            409: {
                "model": HTTPError,
                "description": "User exists",
            }
        }
    )
async def read_users_me(customer: UserCustomerIn = Depends(UserCustomerIn)):
    try:
        await UserController.create_customer(customer)
    except:
        raise HTTPException(status_code=400, detail="User already exists")
    return customer