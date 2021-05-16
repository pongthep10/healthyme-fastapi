from datetime import datetime, timedelta
from typing import Optional
from fastapi import APIRouter
from fastapi import Depends, FastAPI, HTTPException, status
from passlib.context import CryptContext
from pydantic import BaseModel
import traceback
from src.interfaces.controllers.user_controller import UserController
from src.interfaces.serializers.user_serializer import UserCustomerIn, UserCustomerOut
from src.domain.entities.users_entity import UserEntity
from src.shared.exception import HtmeError

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
    response_model_exclude_unset=True)
async def create_customer(customer: UserCustomerIn):
    if not all(x in customer.email for x in ['@','.']):
        raise HTTPException(status_code=422, detail="Email is not correct")
    try:
        created_customer_entity = await UserController.create_customer(customer)
    except HtmeError as e:
        raise HTTPException(status_code=409, detail=e.message)
    except Exception as e:
        print(traceback.format_exc())
        print(e)
        raise HTTPException(status_code=500, detail="Somethig went worng")
    return created_customer_entity