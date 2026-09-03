from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaymentInitiationPaymentTokenCreateRequest(SdkBaseModel):
    """PaymentInitiationPaymentTokenCreateRequest defines the request schema for
    ``/payment_initiation/payment/token/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    payment_id: str
    """The ``payment_id`` returned from ``/payment_initiation/payment/create``."""


class PaymentInitiationPaymentTokenCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    payment_id: str
