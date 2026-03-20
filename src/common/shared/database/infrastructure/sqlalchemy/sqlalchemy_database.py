from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.common.shared.config.config import Settings
from src.common.shared.database.interfaces.database.database import IDatabase


class SqlalchemyDatabase(IDatabase):
    def __init__(self, settings: Settings) -> None:
        self.__settings = settings

    async def create_session(self) -> AsyncSession:
        """Creates sqlalchemy session"""
        engine: AsyncEngine = create_async_engine(
            self.__settings.Database.POSTGRESQL_URL.get_secret_value()
        )
        return async_sessionmaker(bind=engine, class_=AsyncSession)

    async def get_session(self) -> AsyncGenerator[AsyncEngine, Any]:
        """Get's sqlalchemy session"""

        session: AsyncSession = await self.create_session()
        async with session as se:
            try:
                yield se
            finally:
                await se.close()
