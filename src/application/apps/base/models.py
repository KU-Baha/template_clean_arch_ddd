from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, Integer, MetaData
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import Mapped, mapped_column


@as_declarative()
class Base:
    metadata: MetaData

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class BaseORM(Base):
    __abstract__ = True

    id: Mapped[int | None] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
    deleted_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime,
        nullable=True
    )
