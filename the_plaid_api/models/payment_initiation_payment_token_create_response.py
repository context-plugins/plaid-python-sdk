from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class PaymentInitiationPaymentTokenCreateResponse(SdkBaseModel):
    """PaymentInitiationPaymentTokenCreateResponse defines the response schema for
    ``/payment_initiation/payment/token/create``"""

    payment_token: str
    """A ``payment_token`` that can be provided to Link initialization to enter the payment initiation flow"""

    payment_token_expiration_time: RFC3339DateTime
    """The date and time at which the token will expire, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format. A
    ``payment_token`` expires after 15 minutes."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class PaymentInitiationPaymentTokenCreateResponseDict(TypedDict):
    payment_token: str
    payment_token_expiration_time: RFC3339DateTime
    request_id: str
