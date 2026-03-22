from typing import Protocol

from src.application.modules.user.dto.requests.create_user_request import (
    SCreateUserRequest,
)
from src.application.modules.user.dto.responses.create_user_response import (
    SCreateUserResponse,
)


class ICreateUserUseCase(Protocol):
    async def execute(self, request: SCreateUserRequest) -> SCreateUserResponse: ...
