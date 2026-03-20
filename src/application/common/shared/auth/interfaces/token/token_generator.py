from typing import Protocol

from src.application.common.shared.auth.interfaces.token.sub import Sub


class ITokenGenerator(Protocol):
    """Generates tokens like jwt, token, maybe special custom token"""

    def generator(sub: Sub) -> str: ...
