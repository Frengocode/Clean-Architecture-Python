from enum import Enum


class UserEvents(Enum):
    USER_CREATED_EVENT: str = "user.created"


class UserCacheKeys(Enum):
    GET_USER_CACHE_KEY: str = "get.{user_id}.user"
