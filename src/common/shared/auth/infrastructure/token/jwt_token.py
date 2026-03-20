from src.common.shared.auth.interfaces.token.token_generator import ITokenGenerator
from src.common.shared.auth.interfaces.token.sub import Sub
from src.common.shared.config.config import Settings
from jose import jwt


class JwtTokenGenerator(ITokenGenerator):
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def generator(self, sub: Sub) -> str:
        return jwt.decode(
            sub,
            self.settings.Auth.SECRET_KEY.get_secret_value(),
            algorithms=self.settings.Auth.ALGORITHM,
        )
