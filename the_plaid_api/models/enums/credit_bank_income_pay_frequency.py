from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreditBankIncomePayFrequency(str, Enum):
    """The income pay frequency."""

    WEEKLY = "WEEKLY"
    BIWEEKLY = "BIWEEKLY"
    SEMI_MONTHLY = "SEMI_MONTHLY"
    MONTHLY = "MONTHLY"
    DAILY = "DAILY"
    UNKNOWN = "UNKNOWN"

    __str__ = str.__str__


CreditBankIncomePayFrequencyOrStr: TypeAlias = Annotated[
    CreditBankIncomePayFrequency | str, open_enum_validator(CreditBankIncomePayFrequency)
]
