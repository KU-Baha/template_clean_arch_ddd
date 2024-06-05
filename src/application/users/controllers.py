from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from pydantic import EmailStr

from infrastructure.di.container import Container
from application.users.models import UserORM
from domain.user.dto import CreateUser, User
from domain.user.services import UserService

user_router = APIRouter(prefix='/users', tags=['users'])


@user_router.post('/', response_model=User)
@inject
async def create_user(
    user: CreateUser,
    service: UserService = Depends(Provide[Container.user_service]),
) -> User:
    return await service.create_user(user)


@user_router.patch('/', response_model=User)
@inject
async def update_user(
    _id: int,
    user: User,
    service: UserService = Depends(Provide[Container.user_service]),
) -> User:
    return await service.update_user(_id, **user.dict())


@user_router.get('/', response_model=list[User])
@inject
async def users(
    service: UserService = Depends(Provide[Container.user_service]),
) -> list[User]:
    return await service.get_user_list()


@user_router.get('/{email}', response_model=User)
@inject
async def get_user_by_email(
    email: EmailStr,
    service: UserService = Depends(Provide[Container.user_service]),
) -> User:
    return await service.get_by_email(email)


@user_router.get('/{id}', response_model=User)
@inject
async def get_user_by_id(
    id: int,
    service: UserService = Depends(Provide[Container.user_service]),
) -> User:
    return await service.get_by_id(id)


@user_router.delete('/{id}')
@inject
async def delete_user(
    id: int,
    service: UserService = Depends(Provide[Container.user_service]),
) -> None:
    return await service.delete_user(id)
