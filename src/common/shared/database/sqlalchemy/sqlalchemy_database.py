from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.common.shared.config.config import Settings
from sqlalchemy.orm import DeclarativeBase


class SqlalchemyDatabase:
    def __init__(self, settings: Settings) -> None:
        self.engine: AsyncEngine = create_async_engine(
            settings.Database.POSTGRESQL_URL.get_secret_value()
        )
        self.session_factory: AsyncSession = async_sessionmaker(bind=self.engine)

    async def get_session(self) -> AsyncGenerator[AsyncSession]:
        async with self.session_factory() as session:
            yield session


class Base(DeclarativeBase): ...
