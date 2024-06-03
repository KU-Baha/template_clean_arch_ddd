from typing import AsyncGenerator

from sqlalchemy import orm
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from application.config import settings

url = settings.DATABASE_URL

engine = create_async_engine(
    url,
    pool_pre_ping=True,
    future=True,
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    factory = orm.sessionmaker(  # noqa
        engine,
        class_=AsyncSession,
        autoflush=False,
        expire_on_commit=False,
    )

    async with factory() as session:
        yield session


def get_sync_session() -> orm.scoped_session:
    factory = orm.sessionmaker( # noqa
        engine,
        autoflush=False,
        expire_on_commit=False,
    )
    return orm.scoped_session(factory)
