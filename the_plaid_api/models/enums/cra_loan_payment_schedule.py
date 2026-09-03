from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraLoanPaymentSchedule(str, Enum):
    """The frequency of a loan's payment schedule. ``BIWEEKLY`` represents one payment every two weeks."""

    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    BIWEEKLY = "BIWEEKLY"
    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"
    ANNUALLY = "ANNUALLY"
    OTHER = "OTHER"

    __str__ = str.__str__


CraLoanPaymentScheduleOrStr: TypeAlias = Annotated[
    CraLoanPaymentSchedule | str, open_enum_validator(CraLoanPaymentSchedule)
]
