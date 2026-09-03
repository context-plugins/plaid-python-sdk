from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PayPeriodDetailsPayFrequency(str, Enum):
    """The frequency at which an individual is paid."""

    PAY_FREQUENCY_UNKNOWN = "PAY_FREQUENCY_UNKNOWN"
    PAY_FREQUENCY_WEEKLY = "PAY_FREQUENCY_WEEKLY"
    PAY_FREQUENCY_BIWEEKLY = "PAY_FREQUENCY_BIWEEKLY"
    PAY_FREQUENCY_SEMIMONTHLY = "PAY_FREQUENCY_SEMIMONTHLY"
    PAY_FREQUENCY_MONTHLY = "PAY_FREQUENCY_MONTHLY"

    __str__ = str.__str__


PayPeriodDetailsPayFrequencyOrStr: TypeAlias = Annotated[
    PayPeriodDetailsPayFrequency | str, open_enum_validator(PayPeriodDetailsPayFrequency)
]
