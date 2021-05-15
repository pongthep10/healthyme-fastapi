from src.domain.entities.users_entity import UserEntity
from src.infrastructure.databases.htme.db import DbManager
from src.infrastructure.databases.htme.model import Users, UserCustomers, UserCoachs

class UserInDB(UserEntity):
    class Config:
        orm_mode = True

class UserRepository:
    @staticmethod
    async def create_customer(user:UserEntity):
        with DbManager() as db:
            db_user = UserInDB(**user)
            await db.query(db_user)
            await db.refresh(db_user)
        print(db_user)
        return db_user


    # id: Union[str, UUID]
    # username: Optional[str] = ''
    # email: Optional[str] = ''
    # tel: Optional[str] = ''
    # password: Optional[str] = ''
    # is_active: Optional[bool] = ''
    # is_admin: Optional[bool] = ''
    # is_coach: Optional[bool] = ''
    # is_customer: Optional[bool] = ''
    # user_customer_id: Union[str, UUID]
    # user_coach_id: Union[str, UUID]
