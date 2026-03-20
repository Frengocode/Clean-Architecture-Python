from dataclasses import dataclass


@dataclass(frozen=True)
class Email:
    _value: str

    def __post_init__(self):
        if not self._value.endswith("@gmail.com"):
            raise ValueError("Invalid email")

    @property
    def value(self) -> str:
        return self._value
