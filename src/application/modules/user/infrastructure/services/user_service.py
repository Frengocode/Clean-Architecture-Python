from typing import Any, List

from loguru import logger

from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.interfaces.repository.user_repository import (
    IUserRepository,
)
from src.application.modules.user.domain.interfaces.services.user_service import (
    IUserService,
)
from src.application.modules.user.domain.value_objects.email import Email
from src.application.modules.user.domain.value_objects.user_id import UserId
from src.application.modules.user.domain.value_objects.username import Username
from src.application.modules.user.dto.requests.create_user_request import (
    CreateUserRequest,
)
from src.application.modules.user.exceptions.exceptions import (
    UserNotFoundException,
    ExistUserException,
)
from src.application.modules.user.dto.requests.get_users_request import GetUsersRequest


class UserService(IUserService):
    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    async def create_user(self, request: CreateUserRequest) -> User:

        # Verifies exist user by email
        await self.__exist_user(Email(request.email))
        user: User = User(
            id=UserId.generate_unique_id(),
            email=request.email,
            username=request.username,
            password=request.password,
        )
        created_user: User = await self.repository.create_user(user=user)
        logger.info(
            "[UserService.create_user] was created successfully | ID| %s",
            created_user.id,
        )
        return created_user

    async def get_user(self, user_id: UserId) -> User:
        return await self.__get_user_or_404(id=UserId(user_id))

    async def get_user_by_email(self, email: Email) -> User:
        return await self.__get_user_or_404(email=Email(email))

    async def get_user_by_username(self, username: Username) -> User:
        return await self.__get_user_or_404(username=username)

    async def get_users(self, request: GetUsersRequest) -> List[User]:
        logger.info("[UserService.get_users] Getting users %s", request)
        return await self.repository.get_users(request=request)

    async def __exist_user(self, email: Email) -> None:
        user: User = await self.repository.get_user_by_email(email=email)
        if user:
            logger.info("[UserService.__exist_user] Exist user was found %s", email)
            raise ExistUserException

    async def __get_user_or_404(self, **filters: Any) -> User:
        user: User | None = await self.repository.__get_user(**filters)
        if user is None:
            logger.info("[UserService.__get_user_or_404] User not found %s", **filters)
            raise UserNotFoundException()

        logger.info("[UserService.__get_user_or_404] User was found %s", **filters)
        return user
