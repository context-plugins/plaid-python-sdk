from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OriginatorExpectedTransferFrequency(str, Enum):
    """The originator's expected transfer frequency."""

    ONCE_PER_MONTH = "once_per_month"
    TWICE_PER_MONTH = "twice_per_month"
    ONCE_PER_WEEK = "once_per_week"
    DAILY = "daily"

    __str__ = str.__str__


OriginatorExpectedTransferFrequencyOrStr: TypeAlias = Annotated[
    OriginatorExpectedTransferFrequency | str, open_enum_validator(OriginatorExpectedTransferFrequency)
]
