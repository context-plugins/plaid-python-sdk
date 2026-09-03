from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentConsentPeriodicAlignment(str, Enum):
    """Where the payment consent period should start.

    If the institution is Monzo, only ``CONSENT`` alignments are supported.

    ``CALENDAR``: line up with a calendar.

    ``CONSENT``: on the date of consent creation."""

    CALENDAR = "CALENDAR"
    CONSENT = "CONSENT"

    __str__ = str.__str__


PaymentConsentPeriodicAlignmentOrStr: TypeAlias = Annotated[
    PaymentConsentPeriodicAlignment | str, open_enum_validator(PaymentConsentPeriodicAlignment)
]
