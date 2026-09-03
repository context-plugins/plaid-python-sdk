from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NotificationPayloadIdType(str, Enum):
    """Type of entity causing origination of a notification"""

    ACCOUNT = "ACCOUNT"
    CUSTOMER = "CUSTOMER"
    PARTY = "PARTY"
    MAINTENANCE = "MAINTENANCE"
    CONSENT = "CONSENT"

    __str__ = str.__str__


NotificationPayloadIdTypeOrStr: TypeAlias = Annotated[
    NotificationPayloadIdType | str, open_enum_validator(NotificationPayloadIdType)
]
