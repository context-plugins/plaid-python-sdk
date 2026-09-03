from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraVerificationIncomePayFrequency(str, Enum):
    """The income pay frequency. ``WEEKLY``: Weekly pay frequency. ``BIWEEKLY``: Biweekly pay frequency.
    ``SEMI_MONTHLY``: Semi-monthly pay frequency. ``MONTHLY``: Monthly pay frequency. ``DAILY``: Daily pay frequency.
    ``UNKNOWN``: Pay frequency is unknown."""

    WEEKLY = "WEEKLY"
    BIWEEKLY = "BIWEEKLY"
    SEMI_MONTHLY = "SEMI_MONTHLY"
    MONTHLY = "MONTHLY"
    DAILY = "DAILY"
    UNKNOWN = "UNKNOWN"

    __str__ = str.__str__


CraVerificationIncomePayFrequencyOrStr: TypeAlias = Annotated[
    CraVerificationIncomePayFrequency | str, open_enum_validator(CraVerificationIncomePayFrequency)
]
