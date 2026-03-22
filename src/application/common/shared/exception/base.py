from dataclasses import dataclass

from fastapi import HTTPException


@dataclass
class BaseException(HTTPException):
    """Base Exception builder"""

    detail: str
    code: str

    def __init__(
        self,
    ) -> None:
        super().__init__(self.code, self.detail)
