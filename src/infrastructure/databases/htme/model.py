from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, text, Table
from src.infrastructure.databases.htme.config import metadata


Users = Table(
    "users",
    metadata,
    Column('id', String, primary_key=True, server_default=text("uuid_generate_v4()")),
    Column('username', String, unique=True, index=True),
    Column('email', String, unique=True, index=True),
    Column('tel', String, unique=True, index=True),
    Column('password', String),
    Column('is_active', Boolean, default=False),
    Column('is_admin', Boolean, default=False),
    Column('is_coach', Boolean, default=False),
    Column('is_customer', Boolean, default=False),
    Column('user_customer_id', Integer, ForeignKey("user_customers.id")),
    Column('user_coach_id', Integer, ForeignKey("user_coachs.id")),
)


UserCustomers = Table(
    'user_customers',
    metadata,
    Column('id', String, primary_key=True, server_default=text("uuid_generate_v4()")),
)


UserCoachs = Table(
    'user_coachs',
    metadata,
    Column('id', String, primary_key=True, server_default=text("uuid_generate_v4()")),
)



# query = Users.insert().values(email='pongthep11@msd', username='usernamehere',password='passsss')

# from asgiref.sync import async_to_sync
# async_to_sync(db_execute)(query)
# class User(Base):
#     __tablename__ = "users"

#     id = Column(String, primary_key=True, server_default=text("uuid_generate_v4()"))
#     email = Column(String, unique=True, index=True)
#     tel = Column(String, unique=True, index=True)
#     password = Column(String)
#     is_active = Column(Boolean, default=False)
#     is_admin = Column(Boolean, default=False)
#     is_coach = Column(Boolean, default=False)
#     is_customer = Column(Boolean, default=False)
#     user_customer_id = Column(Integer, ForeignKey("user_customers.id"))
#     user_coach_id = Column(Integer, ForeignKey("user_coachs.id"))
    
#     user_customer = relationship("UserCustomer", back_populates="parent")
#     user_coach = relationship("UserCoach", back_populates="parent")



# from typing import List, Optional

# from pydantic import BaseModel

# class AUserBase(BaseModel):
#     email: str


# class AUserCreate(AUserBase):
#     password: str


# class AUser(AUserBase):
#     id: Optional[str]
#     email: str
#     password: str
#     # is_active: bool
#     # is_customer: bool

#     class Config:
#         orm_mode = True


# from sqlalchemy.orm import Session
# from fastapi import Depends
# from src.infrastructure.databases.htme.config import SessionLocal, engine
# def get_user(db: Session, user_id: int):
#     return db.query(User).filter(User.id == user_id).first()

# async def crud_create_user(db: Session, user: AUserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = User(email=user.email, password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     db.close()
#     return db_user

# # Dependency
# def get_db(db=SessionLocal):
#     try:
#         yield db
#     finally:
#         db.close()

# async def create_user(user: AUserCreate, db: Session):
#     # db_user = crud.get_user_by_email(db, email=user.email)
#     # if db_user:
#     #     raise HTTPException(status_code=400, detail="Email already registered")
#     x= await crud_create_user(db=await db(), user=user)
#     print(x)
#     return x


# NewUser = AUserCreate(email='pongthep@gmail.com', password="123123123fdsfllk")

# import asyncio
# loop = asyncio.get_event_loop()
# tasks = [Base.metadata.create_all(bind=engine), create_user(NewUser, SessionLocal)]


# print("Get first result:")
# finished, unfinished = loop.run_until_complete(asyncio.wait(tasks))
