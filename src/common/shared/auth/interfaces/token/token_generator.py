from typing import Protocol


class ITokenGenerator(Protocol):
    """Generates tokens like jwt, token, maybe special custom token"""

    def generator(sub: int) -> str: ...
