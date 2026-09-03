from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MonitoringItemStatusCode(str, Enum):
    """Enum for the status of the Item's insights"""

    AVAILABLE = "AVAILABLE"
    FAILED = "FAILED"
    PENDING = "PENDING"

    __str__ = str.__str__


MonitoringItemStatusCodeOrStr: TypeAlias = Annotated[
    MonitoringItemStatusCode | str, open_enum_validator(MonitoringItemStatusCode)
]
