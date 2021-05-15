from fastapi import HTTPException
from typing import Optional
from src.use_cases.user_use_cases.create_user_use_case import CreateUserUseCase
from src.infrastructure.repositories.user_repository import UserRepository

class UserController:
    def __init__(self):
        self.customer_repository = CustomerRepository()
        self.customer_user_case = CustomerUseCase(
            customer_repository=self.customer_repository)

    @classmethod
    async def create_customer(self, user):
        create_user_use_case = CreateUserUseCase(UserRepository)

    async def get_customer_history_by_id(
            self, customer_id: str,
            next_token: Optional[str] = None):
        try:
            if next_token:
                customer_history, nextToken = (
                    await self.customer_user_case.get_customer_history_by_id(
                        customer_id=customer_id,
                        next_token=next_token
                    ))
            else:
                customer_history, nextToken = (
                    await self.customer_user_case.get_customer_history_by_id(
                        customer_id=customer_id
                    ))
        except Exception as e:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, e.args)
            raise HTTPException(
                status_code=500,
                detail=message
            )
        try:
            pass
        except Exception as e:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, e.args)
            raise HTTPException(
                status_code=500,
                detail=message
            )
        return result
