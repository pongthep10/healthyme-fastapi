from src.domain.entities.users_entity import UserEntity
from src.shared.exception import HtmeError

class CreateUserCustomerUseCase:
    def __init__(self, user_repository, user_entity:UserEntity):
        self.__user_repository = user_repository
        self.__user_entity = user_entity
        self.__user_email_as_username_bool = True
        self.__user_entity.is_customer = True

    async def process(self):
        existing_user_entity = await self.__user_repository.get_user_by_username_or_email(self.__user_entity.username, self.__user_entity.email)
        if existing_user_entity.id:
            raise HtmeError('User exists')

        if self.__user_email_as_username_bool:
            self.__user_entity.username = self.__user_entity.email

            created_user_entity = await self.__user_repository.create_customer(self.__user_entity)
            return created_user_entity

    async def _get_user(self):
        get_user_entity = self.__user_repository.get()