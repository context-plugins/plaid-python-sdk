from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.payment_consent_periodic_alignment import PaymentConsentPeriodicAlignmentOrStr
from .enums.payment_consent_periodic_interval import PaymentConsentPeriodicIntervalOrStr
from .payment_amount import PaymentAmount, PaymentAmountDict


class PaymentConsentPeriodicAmount(SdkBaseModel):
    """Defines consent payments limitations per period."""

    amount: PaymentAmount
    """Maximum cumulative amount for all payments in the specified interval."""

    interval: PaymentConsentPeriodicIntervalOrStr
    """Payment consent periodic interval."""

    alignment: PaymentConsentPeriodicAlignmentOrStr
    """Where the payment consent period should start.

    If the institution is Monzo, only ``CONSENT`` alignments are supported.

    ``CALENDAR``: line up with a calendar.

    ``CONSENT``: on the date of consent creation."""


class PaymentConsentPeriodicAmountDict(TypedDict):
    amount: PaymentAmount | PaymentAmountDict
    interval: PaymentConsentPeriodicIntervalOrStr
    alignment: PaymentConsentPeriodicAlignmentOrStr
