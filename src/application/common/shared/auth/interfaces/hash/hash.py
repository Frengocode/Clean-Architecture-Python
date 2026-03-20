from typing import Protocol


class IHash(Protocol):
    """Hashes value, verifies hash with plain value"""

    def hash_value(value: str) -> str: ...

    """ Hashes value """

    def verify_plain_value(plain_value: str, hash: str) -> bool: ...

    """ Verifies mathing plain value with hash """
