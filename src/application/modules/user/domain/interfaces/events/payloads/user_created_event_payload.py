from dataclasses import dataclass


@dataclass(frozen=True)
class UserCreatedEventPayload:
    id: int
    email: str
