from application.apps.users.models import UserORM
from domain.base.service import BaseService
from domain.user.entities import CreateUser
from domain.user.repositories import IUserRepository


class UserService(BaseService):
    def __init__(
        self,
        user_repository: IUserRepository,
        *args,
        **kwargs
    ):
        self._user_repository = user_repository
        super().__init__(*args, **kwargs)

    async def create_user(self, user: CreateUser) -> UserORM:
        return await self._user_repository.create_user(user)

    async def update_user(self, _id: int, **kwargs) -> UserORM:
        return await self._user_repository.update_user(_id, **kwargs)

    async def get_user_list(self) -> list[UserORM]:
        return await self._user_repository.get_all()

    async def get_by_email(self, email: str) -> UserORM:
        return await self._user_repository.get_by_email(email)

    async def get_by_id(self, _id: int) -> UserORM:
        return await self._user_repository.get_by_id(_id)

    async def delete_user(self, _id: int) -> None:
        return await self._user_repository.delete_user(_id)
