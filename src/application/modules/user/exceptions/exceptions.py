from src.application.common.shared.exception.base import BaseException


class ExistUserException(BaseException):
    code: int = 400
    detail: str = "User already exist by email"


class UserNotFoundException(BaseException):
    code: int = 404
    detail: str = "User not found"
