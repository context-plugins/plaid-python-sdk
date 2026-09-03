from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentConsentPeriodicInterval(str, Enum):
    """Payment consent periodic interval."""

    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    YEAR = "YEAR"

    __str__ = str.__str__


PaymentConsentPeriodicIntervalOrStr: TypeAlias = Annotated[
    PaymentConsentPeriodicInterval | str, open_enum_validator(PaymentConsentPeriodicInterval)
]
