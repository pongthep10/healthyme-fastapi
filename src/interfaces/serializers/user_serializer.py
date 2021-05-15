from pydantic import BaseModel

class UserCustomerIn(BaseModel):
    username: str
    password: str
    email: str

class UserCustomerOut(BaseModel):
    username: str
    email: str