from typing import Protocol

from src.application.modules.user.domain.interfaces.events.payloads.user_created_event_payload import (
    UserCreatedEventPayload,
)


class IUserCreatedEvent(Protocol):

    async def publish_event(self, payload: UserCreatedEventPayload) -> None: ...

    """ Publishes event into broker like  (Kafka, RabbitMQ, Redis Nats and more other)"""
