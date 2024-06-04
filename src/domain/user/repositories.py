from abc import ABC, abstractmethod
from typing import TypeVar

from domain.user.dto import CreateUser, User

model = TypeVar('model')


class IUserRepository(ABC):
    @abstractmethod
    async def create_user(self, user: CreateUser) -> model:
        ...

    @abstractmethod
    async def update_user(self, _id: int, **kwargs) -> model:
        ...

    @abstractmethod
    async def get_by_email(self, email: str) -> model:
        ...

    @abstractmethod
    async def get_by_id(self, _id: int) -> model:
        ...

    @abstractmethod
    async def get_all(self) -> list[model]:
        ...

    @abstractmethod
    async def delete_user(self, _id: int) -> None:
        ...
