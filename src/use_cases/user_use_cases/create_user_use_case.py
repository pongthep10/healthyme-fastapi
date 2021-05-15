from src.domain.entities.users_entity import UserEntity

class CreateUserUseCase:
    def __init__(self, user_repository, user:UserEntity):
        self.__user_repository = __user_repository

    def process(self):
        self.__user_repository.create_customer()