from src.domain.entities.users_entity import UserEntity, UserCustomerEntity

user = UserEntity(id='123')
cus = UserCustomerEntity(**user.dict())

print(cus)