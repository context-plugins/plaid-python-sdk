from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RiskLevel(str, Enum):
    """Risk level for the given risk check type."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    __str__ = str.__str__


RiskLevelOrStr: TypeAlias = Annotated[RiskLevel | str, open_enum_validator(RiskLevel)]
