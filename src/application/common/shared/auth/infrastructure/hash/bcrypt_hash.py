from passlib.context import CryptContext

from src.application.common.shared.auth.interfaces.hash.hash import IHash


class BcryptHash(IHash):
    def __init__(self, context: CryptContext) -> None:
        self.context = context

    def hash_value(self, value: str) -> str:
        return self.context.hash(value)

    def verify_plain_value(self, plain_value: str, hash: str) -> bool:
        isMatchs: bool = self.context.verify(plain_value, hash)
        return isMatchs
