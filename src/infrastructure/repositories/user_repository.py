from src.domain.entities.users_entity import UserEntity
from src.infrastructure.databases.htme.config import database
from src.infrastructure.databases.htme.model import Users, UserCustomers, UserCoachs

class UserRepository:
    @classmethod
    async def create_customer(self, user: UserEntity):
        query = Users.insert().values(
            username = user.username,
            password = user.password,
            email = user.email,
        )
        new_user = await database.execute(query)
        return new_user

    @staticmethod
    async def get_user_by_username(username: str):
        query = "select * from users where username = :username"
        values = {"username": username}
        result = await database.execute(query=query, values=values)
        return result

    @staticmethod
    async def get_user_by_username_or_email(username: str, email: str):
        query = """
            SELECT * from users 
            WHERE username = :username
            OR email = :email
        """
        values = {"username": username, "email": email}
        result = await database.execute(query=query, values=values)
        return result


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
