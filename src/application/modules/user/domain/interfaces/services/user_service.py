from typing import Any, List, Protocol

from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.value_objects.email import Email
from src.application.modules.user.domain.value_objects.user_id import UserId
from src.application.modules.user.domain.value_objects.username import Username
from src.application.modules.user.dto.requests.create_user_request import (
    CreateUserRequest,
)
from src.application.modules.user.dto.requests.get_users_request import GetUsersRequest


class UserService(Protocol):

    async def create_user(self, request: CreateUserRequest) -> User: ...

    async def get_user(self, user_id: UserId) -> User: ...

    async def get_user_by_email(self, email: Email) -> User: ...

    async def get_user_by_username(self, username: Username) -> User: ...

    async def get_users(self, request: GetUsersRequest) -> List[User]: ...

    async def __get_user_or_404(self, **filters: Any) -> User: ...

    """ Get's user or raises 404 not found """
