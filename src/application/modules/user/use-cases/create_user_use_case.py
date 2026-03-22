from loguru import logger

from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.interfaces.events.payloads.user_created_event_payload import (
    UserCreatedEventPayload,
)
from src.application.modules.user.domain.interfaces.events.user_created_event import (
    IUserCreatedEvent,
)
from src.application.modules.user.domain.interfaces.services.user_service import (
    IUserService,
)
from src.application.modules.user.domain.interfaces.use_cases.create_user_use_case import (
    ICreateUserUseCase,
)
from src.application.modules.user.dto.requests.create_user_request import (
    SCreateUserRequest,
)
from src.application.modules.user.dto.responses.create_user_response import (
    SCreateUserResponse,
)


class CreateUserUseCase(ICreateUserUseCase):
    def __init__(
        self, service: IUserService, user_created_event: IUserCreatedEvent
    ) -> None:
        self.service = service
        self.user_created_event = user_created_event

    async def execute(self, request: SCreateUserRequest) -> SCreateUserResponse:
        user: User = await self.service.create_user(request=request)
        await self.__publish_event(user=user)
        logger.info("[CreateUserUseCase] was executed successfully")
        return SCreateUserResponse.model_validate(user)

    async def __publish_event(self, user: User) -> None:
        payload: UserCreatedEventPayload = UserCreatedEventPayload(
            id=user.id.value, email=user.email.value
        )
        await self.user_created_event.publish_event(payload=payload)
