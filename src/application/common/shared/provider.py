from common.shared.database.sqlalchemy.sqlalchemy_database import SqlalchemyDatabase
from dishka import Provider, provide
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.common.shared.auth.infrastructure.hash.bcrypt_hash import (
    BcryptHash,
)
from src.application.common.shared.auth.infrastructure.token.jwt_token import (
    JwtTokenGenerator,
)
from src.application.common.shared.auth.interfaces.hash.hash import IHash
from src.application.common.shared.auth.interfaces.token.token_generator import (
    ITokenGenerator,
)
from src.application.common.shared.config.config import Settings


class SharedProvider(Provider):

    @provide()
    def get_settings(self) -> Settings:
        return Settings()

    @provide()
    def get_crypt_context(self) -> CryptContext:
        return CryptContext(schemes=["bcrypt"])

    @provide()
    def get_hash(self, context: CryptContext) -> IHash:
        return BcryptHash(context=context)

    @provide()
    def get_token_generator(self, settings: Settings) -> ITokenGenerator:
        return JwtTokenGenerator(settings=settings)

    @provide(scope="app")
    async def get_sqlalchemy_database(self, settings: Settings) -> SqlalchemyDatabase:
        return SqlalchemyDatabase(settings=settings)

    @provide()
    async def get_sqlalchemy_session(
        self, database: SqlalchemyDatabase
    ) -> AsyncSession:
        return await database.get_session()
