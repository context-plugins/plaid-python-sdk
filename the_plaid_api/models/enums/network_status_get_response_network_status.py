from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NetworkStatusGetResponseNetworkStatus(str, Enum):
    """Enum representing the overall network status of the user."""

    UNKNOWN = "UNKNOWN"
    RETURNING_USER = "RETURNING_USER"

    __str__ = str.__str__


NetworkStatusGetResponseNetworkStatusOrStr: TypeAlias = Annotated[
    NetworkStatusGetResponseNetworkStatus | str, open_enum_validator(NetworkStatusGetResponseNetworkStatus)
]
