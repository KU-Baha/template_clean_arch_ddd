from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from application.apps.users.models import UserORM
from domain.user.entities import CreateUser
from domain.user.exceptions import UserNotFoundException
from domain.user.repositories import IUserRepository


class UserRepository(IUserRepository):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def create_user(self, user: CreateUser) -> UserORM:
        user = UserORM(
            name=user.name,
            email=user.email,
            password=user.password
        )

        self._session.add(user)
        await self._session.commit()
        await self._session.refresh(user)
        return user

    async def update_user(self, _id, **kwargs) -> UserORM:
        user = await self.get_by_id(_id)

        for key, value in kwargs.items():
            if key == 'deleted_at':
                setattr(user, key, value)
                continue

            if hasattr(user, key) and value:
                setattr(user, key, value)

        await self._session.commit()
        await self._session.refresh(user)
        return user

    async def get_all(self) -> [UserORM]:
        result = await self._session.execute(
            select(UserORM)
        )
        users = result.scalars().all()
        return users

    async def get_by_email(self, email: str) -> UserORM:
        query = select(
            UserORM
        ).where(
            UserORM.email == email
        )

        result = await self._session.execute(query)
        user = result.scalars().first()

        if not user:
            raise UserNotFoundException()

        return user

    async def get_by_id(self, _id: int) -> UserORM:
        query = select(
            UserORM
        ).where(
            UserORM.id == _id
        )
        result = await self._session.execute(query)
        user = result.scalars().first()

        if not user:
            raise UserNotFoundException()

        return user

    async def delete_user(self, _id: int) -> None:
        await self.update_user(_id, deleted_at=datetime.now())
