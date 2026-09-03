from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EarningsBreakdownCanonicalDescription(str, Enum):
    """Commonly used term to describe the earning line item."""

    BONUS = "BONUS"
    COMMISSION = "COMMISSION"
    OVERTIME = "OVERTIME"
    PAID_TIME_OFF = "PAID TIME OFF"
    REGULAR_PAY = "REGULAR PAY"
    VACATION = "VACATION"
    BASIC_ALLOWANCE_HOUSING = "BASIC ALLOWANCE HOUSING"
    BASIC_ALLOWANCE_SUBSISTENCE = "BASIC ALLOWANCE SUBSISTENCE"
    OTHER = "OTHER"

    __str__ = str.__str__


EarningsBreakdownCanonicalDescriptionOrStr: TypeAlias = Annotated[
    EarningsBreakdownCanonicalDescription | str, open_enum_validator(EarningsBreakdownCanonicalDescription)
]
