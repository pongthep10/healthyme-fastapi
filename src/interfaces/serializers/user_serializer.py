from pydantic import BaseModel
from typing import List, Optional, Union, Any
from uuid import UUID
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCustomerIn(BaseModel):
    email: str
    password: str
    fname: str
    lname: str
    tel: Optional[str] = None
    age: Optional[str] = None
    weight_kg: Optional[str] = None
    height_cm: Optional[str] = None

class UserCustomerOut(BaseModel):
    email: str
