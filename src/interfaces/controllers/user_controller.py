from fastapi import HTTPException
from typing import Optional
from src.use_cases.user_use_cases.create_user_use_case import CreateUserCustomerUseCase
from src.infrastructure.repositories.htme_postgres.user_repository import UserRepository
from src.interfaces.serializers.user_serializer import UserCustomerIn
from src.domain.entities.users_entity import UserEntity
from src.infrastructure.webserver.shared.authentication import get_hashed_password

class UserController:
    def __init__(self):
        pass

    @staticmethod
    async def create_customer(requests: UserCustomerIn):
        hashed_password_string = get_hashed_password(requests.password)
        user_entity = UserEntity(email=requests.email, password=hashed_password_string)
        create_user_use_case = CreateUserCustomerUseCase(UserRepository, user_entity)
        return await create_user_use_case.process()