from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .payment_initiation_payment import PaymentInitiationPayment, PaymentInitiationPaymentDict


class PaymentInitiationPaymentListResponse(SdkBaseModel):
    """PaymentInitiationPaymentListResponse defines the response schema for ``/payment_initiation/payment/list``"""

    payments: list[PaymentInitiationPayment]
    """An array of payments that have been created, associated with the given ``client_id``."""

    next_cursor: RFC3339DateTime | None
    """The value that, when used as the optional ``cursor`` parameter to ``/payment_initiation/payment/list``, will
    return the next unreturned payment as its first payment."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class PaymentInitiationPaymentListResponseDict(TypedDict):
    payments: list[PaymentInitiationPaymentDict]
    next_cursor: RFC3339DateTime | None
    request_id: str
