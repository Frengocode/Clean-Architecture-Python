import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class UserId:
    _value: str

    def generate_unique_id(self) -> str:
        """Generates unique user_id"""
        return str(uuid.uuid4())

    @property
    def value(self) -> str:
        self._value
