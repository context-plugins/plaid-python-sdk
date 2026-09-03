from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DashboardUserStatus(str, Enum):
    """The current status of the user."""

    INVITED = "invited"
    ACTIVE = "active"
    DEACTIVATED = "deactivated"

    __str__ = str.__str__


DashboardUserStatusOrStr: TypeAlias = Annotated[DashboardUserStatus | str, open_enum_validator(DashboardUserStatus)]
