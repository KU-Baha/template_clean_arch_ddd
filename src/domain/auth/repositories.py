from abc import ABC, abstractmethod
from typing import Optional

from domain.auth.entities import Token


class IAuthRepository(ABC):
    @abstractmethod
    async def create_token(self, token: Token) -> None:
        pass

    @abstractmethod
    async def get_token(self, token: str) -> Optional[Token]:
        pass

    @abstractmethod
    async def revoke_token(self, token: str) -> None:
        pass

    @abstractmethod
    async def verify_token(self, token: str):
        pass
