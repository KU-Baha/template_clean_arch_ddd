from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from application.base.models import BaseORM


class UserORM(BaseORM):
    __tablename__ = 'user'

    name: Mapped[str] = mapped_column(
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        nullable=False,
        unique=True
    )
    phone_number: Mapped[str] = mapped_column(
        nullable=False,
        unique=True
    )
    password: Mapped[str] = mapped_column(
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        default=True
    )
