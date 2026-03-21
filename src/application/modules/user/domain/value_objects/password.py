from dataclasses import dataclass


@dataclass(frozen=True)
class Password:
    _value: str

    def __post__init__(self) -> None:
        if len(self._value) <= 8:
            raise Exception("Password can't be small 8 word !")

    @property
    def value(self) -> str:
        return self._value
