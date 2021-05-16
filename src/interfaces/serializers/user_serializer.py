from pydantic import BaseModel

class UserCustomerIn(BaseModel):
    email: str
    password: str

class UserCustomerOut(BaseModel):
    email: str