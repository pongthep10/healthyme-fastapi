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
    user_customer_id: Optional[Union[str, UUID]]
    user_coach_id: Optional[Union[str, UUID]]

class UserCustomerEntity(BaseModel):
    id: Optional[Union[str, UUID]] = None
    program_id: Optional[Union[str, UUID]]
    package_id: Optional[Union[str, UUID]]
    course_id: Optional[Union[str, UUID]]
    age: Optional[Union[str, UUID]]
    weight_kg: Optional[float]
    height_cm: Optional[float]