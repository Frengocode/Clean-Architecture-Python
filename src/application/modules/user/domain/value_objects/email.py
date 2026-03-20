from typing import Self


class Email:
    def __init__(self, email: str) -> None:
        self.email = email

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def email(self) -> Self:
        if not self.email.endswith("@gmail.com"):
            raise Exception("Invalid Email")
        return Self
