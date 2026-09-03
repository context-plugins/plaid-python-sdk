from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BusinessWebsiteBuildStatus(str, Enum):
    """Build status of the business website."""

    COMING_SOON = "coming_soon"
    ACTIVE = "active"
    INACTIVE = "inactive"

    __str__ = str.__str__


BusinessWebsiteBuildStatusOrStr: TypeAlias = Annotated[
    BusinessWebsiteBuildStatus | str, open_enum_validator(BusinessWebsiteBuildStatus)
]
