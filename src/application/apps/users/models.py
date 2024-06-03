from sqlmodel import Field

from application.apps.base.models import BaseORM


class UserORM(BaseORM, table=True):
    name: str = Field(
        nullable=False
    )
    email: str = Field(
        nullable=False,
        unique=True
    )
    phone_number: str = Field(
        nullable=False,
        unique=True
    )
    password: str = Field(
        nullable=False
    )
    is_active: bool = Field(
        default=True
    )
