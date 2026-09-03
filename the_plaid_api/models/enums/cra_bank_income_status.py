from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraBankIncomeStatus(str, Enum):
    """The status of the income sources. ``ACTIVE``: The income source is active. ``INACTIVE``: The income source is
    inactive. ``UNKNOWN``: The income source status is unknown."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    UNKNOWN = "UNKNOWN"

    __str__ = str.__str__


CraBankIncomeStatusOrStr: TypeAlias = Annotated[CraBankIncomeStatus | str, open_enum_validator(CraBankIncomeStatus)]
