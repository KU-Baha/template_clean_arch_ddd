from datetime import datetime, timedelta

import jwt

from application.config import jwt_settings
from domain.auth.entities import AccessToken, RefreshToken
from domain.auth.exceptions import DecodeTokenException, ExpiredTokenException, InvalidTokenException


class JWTService:
    def create_access_token(self, user_id: str) -> str:
        expires_at = datetime.utcnow() + timedelta(minutes=jwt_settings.ACCESS_TOKEN_EXPIRE)
        access_token_payload = AccessToken(sub=user_id, exp=expires_at)

        access_token = jwt.encode(
            access_token_payload.dict(),
            jwt_settings.SECRET_KEY,
            algorithm=jwt_settings.ALGORITHM
        )
        return access_token

    def create_refresh_token(self, user_id: str) -> str:
        expires_at = datetime.utcnow() + timedelta(days=jwt_settings.REFRESH_TOKEN_EXPIRE)
        refresh_token_payload = RefreshToken(sub=user_id, exp=expires_at)

        refresh_token = jwt.encode(
            refresh_token_payload.dict(),
            jwt_settings.SECRET_KEY,
            algorithm=jwt_settings.ALGORITHM
        )

        return refresh_token

    def verify_token(self, token):
        try:
            jwt.decode(
                token,
                jwt_settings.SECRET_KEY,
                algorithms=[jwt_settings.ALGORITHM]
            )
        except jwt.exceptions.ExpiredSignatureError:
            raise ExpiredTokenException(
                message="Token has expired"
            )

    def refresh_access_token(self, refresh_token: str) -> str | None:
        try:
            payload = jwt.decode(
                refresh_token,
                jwt_settings.SECRET_KEY,
                algorithms=[jwt_settings.ALGORITHM]
            )
            user_id = payload.get("sub")

            if not user_id:
                raise DecodeTokenException(
                    message="Token decode error"
                )

            user = self._user_repository.get_by_id(user_id)
            return self.create_access_token(str(user.id))

        except jwt.exceptions.ExpiredSignatureError:
            raise ExpiredTokenException(
                message="Token has expired"
            )
        except jwt.exceptions.InvalidTokenError:
            raise InvalidTokenException(
                message="Invalid token"
            )
