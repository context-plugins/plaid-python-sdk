from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PayFrequencyValue(str, Enum):
    """The frequency of the pay period."""

    MONTHLY = "monthly"
    SEMIMONTHLY = "semimonthly"
    WEEKLY = "weekly"
    BIWEEKLY = "biweekly"
    UNKNOWN = "unknown"

    __str__ = str.__str__


PayFrequencyValueOrStr: TypeAlias = Annotated[PayFrequencyValue | str, open_enum_validator(PayFrequencyValue)]
