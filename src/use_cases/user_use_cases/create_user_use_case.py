from src.domain.entities.users_entity import UserEntity

class CreateUserUseCase:
    def __init__(self, user_repository, user:UserEntity):
        self.__user_repository = user_repository
        self.__user = user

    async def process(self):
        existing_user_id = await self.__user_repository.get_user_by_username_or_email(self.__user.username, self.__user.email)
        if existing_user_id:
            raise Exception('User exist')
        created_user_entity = await self.__user_repository.create_customer(self.__user)
        return created_user_entity

    async def _get_user(self):
        get_user_entity = self.__user_repository.get()