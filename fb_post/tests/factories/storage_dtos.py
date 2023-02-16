import factory

from fb_post.interactors.storage_interfaces.dtos import UserDTO, UsersDTO, \
    UsersCountDTO


class UserDTOFactory(factory.Factory):
    class Meta:
        model = UserDTO

    user_id = factory.sequence(lambda n: n + 1)
    name = factory.Sequence(lambda n: f"User_{n + 1}")
    profile_pic = factory.Sequence(
        lambda n: f"https://profile_pic_url{n + 1}.com")


class UsersCountDTOFactory(factory.Factory):
    class Meta:
        model = UsersCountDTO
    users_count = factory.sequence(lambda n: n + 1)


class UsersDTOFactory(factory.Factory):
    class Meta:
        model = UsersDTO

    user_dtos = factory.List([
        factory.SubFactory(UserDTOFactory) for i in range(1)
    ])
    users_count_dto = factory.List([
        factory.SubFactory(UsersCountDTOFactory) for i in range(1)
    ])
