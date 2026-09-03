from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RiskLevelWithNoData(str, Enum):
    """Risk level for the given risk check type, when available."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    NO_DATA = "no_data"

    __str__ = str.__str__


RiskLevelWithNoDataOrStr: TypeAlias = Annotated[RiskLevelWithNoData | str, open_enum_validator(RiskLevelWithNoData)]
