from typing import List, Optional, Union, Any
from uuid import UUID
from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserEntity(BaseModel):
    id: Optional[Union[str, UUID]] = None
    username: Optional[str] = None
    email: Optional[str] = None
    tel: Optional[str] = None
    password: Optional[str] = None
    fname: Optional[str] = None
    lname: Optional[str] = None
    display_image_url: Optional[str] = None
    is_active: Optional[bool] = False
    is_admin: Optional[bool] = False
    is_customer: Optional[bool] = False
    is_coach: Optional[bool] = False
    age: Optional[Union[str, UUID]]
    weight_kg: Optional[float]
    height_cm: Optional[float]
