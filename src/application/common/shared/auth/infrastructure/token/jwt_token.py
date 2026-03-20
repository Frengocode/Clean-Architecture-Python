from jose import jwt

from src.application.common.shared.auth.interfaces.token.sub import Sub
from src.application.common.shared.auth.interfaces.token.token_generator import (
    ITokenGenerator,
)
from src.application.common.shared.config.config import Settings


class JwtTokenGenerator(ITokenGenerator):
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def generator(self, sub: Sub) -> str:
        """Generates jwt token by sub"""
        return jwt.decode(
            sub,
            self.settings.Auth.SECRET_KEY.get_secret_value(),
            algorithms=self.settings.Auth.ALGORITHM,
        )
