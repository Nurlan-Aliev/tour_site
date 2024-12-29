from redis import Redis
from asyncio import current_task
from settings import settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)

r = Redis(
    host=settings.RE_HOST,
    port=settings.RE_PORT,
    decode_responses=True,
)


class Base(DeclarativeBase):
    pass


class DataBaseHelper:
    def __init__(self, url, echo=False):
        self.async_engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.async_session_factory = async_sessionmaker(
            self.async_engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def get_scoped_session(self):

        session = async_scoped_session(
            session_factory=self.async_session_factory,
            scopefunc=current_task,
        )
        return session

    async def scope_session_dependency(self) -> AsyncSession:

        async with self.get_scoped_session() as s:
            yield s


db_helper = DataBaseHelper(
    settings.db_connect,
)
