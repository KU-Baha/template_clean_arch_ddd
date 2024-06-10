import hashlib

from domain.auth.entities import Token
from domain.auth.repositories import IAuthRepository
from domain.auth.services.jwt_service import JWTService
from domain.base.service import BaseService
from domain.user.dto import CreateUser
from domain.user.services import UserService


class AuthService(BaseService, JWTService):
    def __init__(
        self,
        auth_repository: IAuthRepository,
        user_service: UserService,
        *args,
        **kwargs
    ):
        self._auth_repository = auth_repository
        self._user_service = user_service
        super().__init__(*args, **kwargs)

    async def register(self, name: str, email: str, password: str) -> Token:
        hashed_password = await self.hash_password(password)

        user = CreateUser(
            name=name,
            email=email,
            password=hashed_password
        )

        await self._user_service.create_user(user)
        return await self.login(email, password)

    async def login(self, email: str, password: str) -> Token | None:
        user = await self._user_service.get_by_email(email)

        if not (user and self.verify_password(password, user.password)):
            return

        access_token = self.create_access_token(str(user.id))
        refresh_token = self.create_refresh_token(str(user.id))

        return Token(
            access_token=access_token,
            token_type="bearer",
            refresh_token=refresh_token
        )

    async def logout(self, token_str: str) -> None:
        await self._auth_repository.revoke_token(token_str)

    async def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return await self.hash_password(plain_password) == hashed_password

    @staticmethod
    async def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()
