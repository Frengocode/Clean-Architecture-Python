from dishka import Provider, provide
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext

from src.common.shared.auth.interfaces.hash.hash import IHash
from src.common.shared.auth.infrastructure.hash.bcrypt_hash import BcryptHash

from src.common.shared.auth.interfaces.token.token_generator import ITokenGenerator
from src.common.shared.auth.infrastructure.token.jwt_token import JwtTokenGenerator


from src.common.shared.config.config import Settings

from src.common.shared.database.infrastructure.sqlalchemy.sqlalchemy_database import (
    SqlalchemyDatabase,
)


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

    @provide()
    async def get_sqlalchemy_session(self, settings: Settings) -> AsyncSession:
        sqlalchemy_database: SqlalchemyDatabase = SqlalchemyDatabase(settings=settings)
        return await sqlalchemy_database.get_session()
