from abc import ABC, abstractmethod
from typing import Any, List

from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.value_objects.email import Email
from src.application.modules.user.domain.value_objects.user_id import UserId
from src.application.modules.user.domain.value_objects.username import Username
from src.application.modules.user.dto.requests.get_users_request import GetUsersRequest


class IUserRepository(ABC):
    """User repository abstraction"""

    @abstractmethod
    async def create_user(self, user: User) -> User: ...

    @abstractmethod
    async def _get_user(self, **filters: Any) -> User | None: ...

    """ _get_user is a prviate method, uses at -> get_user_by_id, get_user_by_username, get_user_by_email  """

    @abstractmethod
    async def get_user_by_id(self, userId: UserId) -> User | None: ...

    @abstractmethod
    async def get_user_by_username(self, username: Username) -> User | None: ...

    @abstractmethod
    async def get_user_by_email(self, email: Email) -> User | None: ...

    @abstractmethod
    async def get_users(self, request: GetUsersRequest) -> List[User]: ...
