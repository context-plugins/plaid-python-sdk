from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FdxEventStatus(str, Enum):
    """Current status of indicated entity after reported event change. Not all statuses will be supported on all entity
    types by all data providers"""

    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    REVOKED = "REVOKED"
    SUSPENDED = "SUSPENDED"

    __str__ = str.__str__


FdxEventStatusOrStr: TypeAlias = Annotated[FdxEventStatus | str, open_enum_validator(FdxEventStatus)]
