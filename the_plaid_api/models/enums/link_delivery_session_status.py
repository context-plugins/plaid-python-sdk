from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LinkDeliverySessionStatus(str, Enum):
    """The status of the given Hosted Link session.

    ``CREATED``: The session is created but not yet accessed by the user

    ``OPENED``: The session is opened by the user but not yet completed

    ``EXITED``: The session has been exited by the user

    ``COMPLETED``: The session has been completed by the user

    ``EXPIRED``: The session has expired"""

    CREATED = "CREATED"
    OPENED = "OPENED"
    EXITED = "EXITED"
    COMPLETED = "COMPLETED"
    EXPIRED = "EXPIRED"

    __str__ = str.__str__


LinkDeliverySessionStatusOrStr: TypeAlias = Annotated[
    LinkDeliverySessionStatus | str, open_enum_validator(LinkDeliverySessionStatus)
]
