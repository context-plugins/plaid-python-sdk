from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NotificationCategory(str, Enum):
    """Category of Notification"""

    SECURITY = "SECURITY"
    MAINTENANCE = "MAINTENANCE"
    FRAUD = "FRAUD"
    CONSENT = "CONSENT"
    NEW_DATA = "NEW_DATA"
    TOKENIZED_ACCOUNT_NUMBER = "TOKENIZED_ACCOUNT_NUMBER"

    __str__ = str.__str__


NotificationCategoryOrStr: TypeAlias = Annotated[NotificationCategory | str, open_enum_validator(NotificationCategory)]
