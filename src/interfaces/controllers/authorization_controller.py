from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, HTTPException, status
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel


class AuthorizationController:
    def __init__(self):
        pass

    @staticmethod
    async def get_token(form_data):
        user_entity = UserEntity(username=requests.username, password=requests.password)
        create_user_use_case = CreateUserUseCase(UserRepository, user_entity)
        return await create_user_use_case.process()