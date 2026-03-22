from aiokafka import AIOKafkaProducer
from dishka import Provider, provide
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.common.shared.auth.interfaces.hash.hash import IHash
from src.application.modules.user.domain.interfaces.events.user_created_event import (
    IUserCreatedEvent,
)
from src.application.modules.user.domain.interfaces.repository.user_repository import (
    IUserRepository,
)
from src.application.modules.user.domain.interfaces.services.user_service import (
    IUserService,
)
from src.application.modules.user.domain.interfaces.use_cases.create_user_use_case import (
    ICreateUserUseCase,
)
from src.application.modules.user.infrastructure.events.user_created_event import (
    UserCreatedEvent,
)
from src.application.modules.user.infrastructure.repository.user_repository import (
    UserRepository,
)
from src.application.modules.user.infrastructure.services.user_service import (
    UserService,
)
from src.application.modules.user.use_cases.create_user_use_case import (
    CreateUserUseCase,
)


class UserProvider(Provider):

    @provide
    def get_user_repository(self, session: AsyncSession) -> IUserRepository:
        return UserRepository(session=session)

    @provide
    def get_user_service(self, repository: IUserRepository) -> IUserService:
        return UserService(repository=repository)

    @provide
    def get_user_created_event(self, producer: AIOKafkaProducer) -> IUserCreatedEvent:
        return UserCreatedEvent(producer=producer)

    @provide
    def get_create_user_use_case(
        self, service: IUserService, user_created_event: IUserCreatedEvent, hash: IHash
    ) -> ICreateUserUseCase:
        return CreateUserUseCase(
            service=service, user_created_event=user_created_event, hash=hash
        )
