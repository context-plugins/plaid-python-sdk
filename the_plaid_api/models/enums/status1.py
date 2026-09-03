from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status1(str, Enum):
    """The status of the incident."""

    INVESTIGATING = "INVESTIGATING"
    IDENTIFIED = "IDENTIFIED"
    SCHEDULED = "SCHEDULED"
    RESOLVED = "RESOLVED"
    UNKNOWN = "UNKNOWN"

    __str__ = str.__str__


Status1OrStr: TypeAlias = Annotated[Status1 | str, open_enum_validator(Status1)]
