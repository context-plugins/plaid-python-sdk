from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IssuesStatus(str, Enum):
    """The current status of the issue."""

    REPORTED = "REPORTED"
    AWAITING_RESOLUTION = "AWAITING_RESOLUTION"
    FIX_IN_PROGRESS = "FIX_IN_PROGRESS"
    FIX_PENDING_VALIDATION = "FIX_PENDING_VALIDATION"
    CANNOT_FIX = "CANNOT_FIX"
    RESOLVED = "RESOLVED"

    __str__ = str.__str__


IssuesStatusOrStr: TypeAlias = Annotated[IssuesStatus | str, open_enum_validator(IssuesStatus)]
