from src.domain.entities.users_entity import UserEntity


sample_user = {
      id:'sadasd',
}
a = UserEntity(*sample_user)
print(a)