from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PaymentInitiationRecipientCreateResponse(SdkBaseModel):
    """PaymentInitiationRecipientCreateResponse defines the response schema for
    ``/payment_initiation/recipient/create``"""

    recipient_id: str
    """A unique ID identifying the recipient"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class PaymentInitiationRecipientCreateResponseDict(TypedDict):
    recipient_id: str
    request_id: str
