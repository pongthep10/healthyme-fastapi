from datetime import datetime, timedelta
from typing import Optional
from fastapi import APIRouter
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from src.interfaces.controllers.user_controller import UserController
from src.domain.entities.users_entity import UserEntity


router = APIRouter(
    prefix="",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

class UserCustomerIn(BaseModel):
    user_name: str
    password: str


@router.get("/customer/create/")
async def read_users_me(customer: UserCustomerIn = Depends(UserCustomerIn)):
    UserController()
    return customer