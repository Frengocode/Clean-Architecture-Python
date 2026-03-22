from typing import Protocol

from src.application.modules.user.domain.interfaces.events.payloads.user_created_event_payload import (
    UserCreatedEventPayload,
)


class IUserCreatedEventHandler(Protocol):

    async def handle(self, payload: UserCreatedEventPayload) -> None: ...

    """ Handles user created event """
