from src.domain.entities.users_entity import UserEntity
from src.infrastructure.databases.htme.config import database
from src.infrastructure.databases.htme.model import Users, UserCustomers, UserCoachs
from src.shared.exception import HtmeError

class UserRepository:
    @classmethod
    async def create_customer(self, user: UserEntity):
        query = Users.insert().values(
            username = user.username,
            password = user.password,
            email = user.email,
        )
        new_user_uuid = await database.execute(query)
        if new_user_uuid:   
            return await UserRepository.get_user_by_id(new_user_uuid)

    @staticmethod
    async def get_user_by_id(id: str):
        query = "SELECT * FROM users WHERE id = :id"
        result = await database.fetch_one(query=query, values={"id": id})
        return UserEntity(**result)

    @staticmethod
    async def get_user_by_email(username: str):
        query = "select * from users where email = :email"
        values = {"email": email}
        result = await database.fetch_all(query=query, values=values)
        return UserEntity(**result)

    @staticmethod
    async def get_user_by_username_or_email(username: str, email: str):
        query = """
            SELECT * from users 
            WHERE username = :username
            OR email = :email
        """
        values = {"username": username, "email": email}
        user_id = await database.execute(query=query, values=values)
        if user_id:
            return UserEntity(id=user_id)
        else:
            return UserEntity()


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
