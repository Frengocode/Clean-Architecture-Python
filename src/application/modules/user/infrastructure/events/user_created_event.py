from aiokafka import AIOKafkaProducer
from loguru import logger

from src.application.modules.user.constants.constants import UserEvents
from src.application.modules.user.domain.interfaces.events.payloads.user_created_event_payload import (
    UserCreatedEventPayload,
)
from src.application.modules.user.domain.interfaces.events.user_created_event import (
    IUserCreatedEvent,
)


class UserCreatedEvent(IUserCreatedEvent):
    def __init__(self, producer: AIOKafkaProducer) -> None:
        self.producer = producer

    async def publish_event(self, payload: UserCreatedEventPayload) -> None:
        await self.producer.send(UserEvents.USER_CREATED_EVENT, payload)
        logger.info("[UserCreatedEvent] Event was successfully published %s", payload)
