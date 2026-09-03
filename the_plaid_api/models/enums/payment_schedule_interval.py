from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentScheduleInterval(str, Enum):
    """The frequency interval of the payment."""

    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"

    __str__ = str.__str__


PaymentScheduleIntervalOrStr: TypeAlias = Annotated[
    PaymentScheduleInterval | str, open_enum_validator(PaymentScheduleInterval)
]
