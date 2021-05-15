from typing import List, Optional, Union, Any
from uuid import UUID
from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserEntity(BaseModel):
    id: Optional[Union[str, UUID]]
    username: Optional[str] = ''
    email: Optional[str] = None
    tel: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = False
    is_admin: Optional[bool] = False
    is_coach: Optional[bool] = False
    is_customer: Optional[bool] = False
    user_customer_id: Optional[Union[str, UUID]]
    user_coach_id: Optional[Union[str, UUID]]