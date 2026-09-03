from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NotificationPriority(str, Enum):
    """Priority of notification"""

    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    __str__ = str.__str__


NotificationPriorityOrStr: TypeAlias = Annotated[NotificationPriority | str, open_enum_validator(NotificationPriority)]
