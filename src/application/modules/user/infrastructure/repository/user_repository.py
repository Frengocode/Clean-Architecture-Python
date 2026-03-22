from typing import Any, List

from sqlalchemy import Result, Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.interfaces.repository.user_repository import (
    IUserRepository,
)
from src.application.modules.user.domain.value_objects.email import Email
from src.application.modules.user.domain.value_objects.user_id import UserId
from src.application.modules.user.domain.value_objects.username import Username
from src.application.modules.user.dto.requests.get_users_request import GetUsersRequest
from src.application.modules.user.infrastructure.models.user import UserModel


class UserRepository(IUserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_user(self, user: User) -> User:
        creating_user: UserModel = UserModel(**user)
        self.session.add(creating_user)
        await self.session.commit()
        await self.session.refresh(creating_user)
        return User(
            id=creating_user.id,
            email=creating_user.email,
            username=creating_user.username,
        )

    async def get_user_by_email(self, email: Email) -> User | None:
        return await self._get_user(email=email.value)

    async def get_user_by_id(self, userId: UserId) -> User | None:
        return await self._get_user(id=userId.value)

    async def get_user_by_username(self, username: Username) -> User | None:
        return await self._get_user(username=username.value)

    async def get_users(self, request: GetUsersRequest) -> List[User]:
        stmt: Select[UserModel] = (
            select(UserModel).offset(request.offset).limit(request.limit)
        )
        result: Result[UserModel] = await self.session.execute(stmt)
        return result.scalars().all()

    async def _get_user(self, **filters: Any) -> User | None:
        stmt: Select[UserModel] = select(UserModel).filter_by(**filters)
        result: Result[UserModel] = await self.session.execute(stmt)
        return result.scalars().first()
