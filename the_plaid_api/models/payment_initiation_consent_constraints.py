from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .payment_amount import PaymentAmount, PaymentAmountDict
from .payment_consent_periodic_amount import PaymentConsentPeriodicAmount, PaymentConsentPeriodicAmountDict
from .payment_consent_valid_date_time import PaymentConsentValidDateTime, PaymentConsentValidDateTimeDict


class PaymentInitiationConsentConstraints(SdkBaseModel):
    """Limitations that will be applied to payments initiated using the payment consent."""

    valid_date_time: OptionalNullable[PaymentConsentValidDateTime] = UNSET
    """Life span for the payment consent. After the ``to`` date the payment consent expires and can no longer be used
    for payment initiation."""

    max_payment_amount: PaymentAmount
    """Maximum amount of a single payment initiated using the payment consent."""

    periodic_amounts: list[PaymentConsentPeriodicAmount]
    """A list of amount limitations per period of time."""


class PaymentInitiationConsentConstraintsDict(TypedDict):
    valid_date_time: NotRequired[PaymentConsentValidDateTimeDict | None]
    max_payment_amount: PaymentAmountDict
    periodic_amounts: list[PaymentConsentPeriodicAmountDict]
