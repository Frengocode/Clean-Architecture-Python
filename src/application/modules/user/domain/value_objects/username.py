from dataclasses import dataclass


@dataclass(frozen=True)
class Username:
    _value: str

    def __post_init__(self) -> None:
        if len(self._value) <= 4:
            raise Exception("Username can't be small than 4 words")

    @property
    def _value(self) -> str:
        return self._value
