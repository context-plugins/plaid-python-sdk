from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferScheduleIntervalUnit(str, Enum):
    """The unit of the recurring interval."""

    WEEK = "week"
    MONTH = "month"

    __str__ = str.__str__


TransferScheduleIntervalUnitOrStr: TypeAlias = Annotated[
    TransferScheduleIntervalUnit | str, open_enum_validator(TransferScheduleIntervalUnit)
]
