from typing import Protocol, TypeVar

T = TypeVar("T")


class IDatabase(Protocol):
    """Each database should implement from that abstraction"""

    async def create_session(self) -> T: ...

    """ Creates session """

    async def get_session(self) -> T: ...

    """ Get's session """
