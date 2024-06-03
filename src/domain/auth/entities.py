from datetime import datetime

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str


class AccessToken(BaseModel):
    sub: str
    exp: datetime


class RefreshToken(BaseModel):
    sub: str
    exp: datetime
