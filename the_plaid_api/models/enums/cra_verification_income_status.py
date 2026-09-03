from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraVerificationIncomeStatus(str, Enum):
    """The status of the income source. ``ACTIVE``: The income source is active. ``INACTIVE``: The income source is
    inactive. ``UNKNOWN``: The income source status is unknown."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    UNKNOWN = "UNKNOWN"

    __str__ = str.__str__


CraVerificationIncomeStatusOrStr: TypeAlias = Annotated[
    CraVerificationIncomeStatus | str, open_enum_validator(CraVerificationIncomeStatus)
]
