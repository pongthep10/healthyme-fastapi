from src.domain.entities.users_entity import UserEntity
from src.infrastructure.databases.htme.config import database
from src.infrastructure.databases.htme.model import Users, UserCustomers, UserCoachs
from src.shared.exception import HtmeError

class UserRepository:
    def __init__(self, user_entity: UserEntity):
        self.__user_entity = user_entity

    async def create_user(self):
        async with database.transaction() as db:
            query = Users.insert().values(
                username = self.__user_entity.username,
                email = self.__user_entity.email,
                password = self.__user_entity.password,
                tel = self.__user_entity.tel,
                fname = self.__user_entity.fname,
                lname = self.__user_entity.lname,
                display_image_url = self.__user_entity.display_image_url,
                is_active = self.__user_entity.is_active,
                age = self.__user_entity.age,
                weight_kg = self.__user_entity.weight_kg,
                height_cm = self.__user_entity.height_cm,
                is_customer = self.__user_entity.is_customer,
                is_admin = self.__user_entity.is_admin,
                is_coach = self.__user_entity.is_coach,
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
    async def get_user_by_username(username: str):
        query = "select * from users where username = :username"
        values = {"username": username}
        user_uuid = await database.execute(query=query, values=values)
        if user_uuid:   
            return await UserRepository.get_user_by_id(user_uuid)
        else:
            return UserEntity()

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



    # async def create_user_customer(self,    : UserCustomers = UserCustomers()):
    #     async with database.transaction() as db:
    #         user_customer_query = UserCustomers.insert().values(
    #                 program_id = user_customer_entity.program_id,
    #                 package_id = user_customer_entity.package_id,
    #                 course_id = user_customer_entity.course_id,
    #                 age = user_customer_entity.age,
    #                 weight_kg = user_customer_entity.weight_kg,
    #                 height_cm = user_customer_entity.height_cm,
    #             )
    #         new_user_customer_uuid = await database.execute(user_customer_query)
    #         new_user_entity = await self.create_user()
    #         user_customer_entity = 

            # if new_user_customer_id:
            #     return await UserRepository.get_user_customer_by_id(new_user_customer_uuid)
