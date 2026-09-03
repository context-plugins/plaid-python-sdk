from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NotificationSeverity(str, Enum):
    """Severity level of notification"""

    EMERGENCY = "EMERGENCY"
    ALERT = "ALERT"
    WARNING = "WARNING"
    NOTICE = "NOTICE"
    INFO = "INFO"

    __str__ = str.__str__


NotificationSeverityOrStr: TypeAlias = Annotated[NotificationSeverity | str, open_enum_validator(NotificationSeverity)]
