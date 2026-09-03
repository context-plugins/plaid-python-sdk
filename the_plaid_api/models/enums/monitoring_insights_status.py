from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MonitoringInsightsStatus(str, Enum):
    """Enum for the status of the insights"""

    AVAILABLE = "AVAILABLE"
    FAILED = "FAILED"

    __str__ = str.__str__


MonitoringInsightsStatusOrStr: TypeAlias = Annotated[
    MonitoringInsightsStatus | str, open_enum_validator(MonitoringInsightsStatus)
]
