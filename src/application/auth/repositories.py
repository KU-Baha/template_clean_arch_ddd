from domain.auth.repositories import IAuthRepository


class AuthRepository(IAuthRepository):
    async def create_token(self, token):
        pass

    async def get_token(self, token):
        pass

    async def revoke_token(self, token):
        pass

    async def verify_token(self, token):
        pass
