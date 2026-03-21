from dataclasses import dataclass
from src.application.modules.user.domain.value_objects.user_id import UserId
from src.application.modules.user.domain.value_objects.email import Email
from src.application.modules.user.domain.value_objects.username import Username


@dataclass(frozen=True, slots=True)
class User:
    id: UserId
    email: Email
    username: Username

    def exist_user(self, email: Email) -> None:
        if self.email.value == email:
            raise Exception("User already exists")
