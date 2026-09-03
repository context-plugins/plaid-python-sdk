from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaymentInitiationRecipientGetRequest(SdkBaseModel):
    """PaymentInitiationRecipientGetRequest defines the request schema for ``/payment_initiation/recipient/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    recipient_id: str
    """The ID of the recipient"""


class PaymentInitiationRecipientGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    recipient_id: str
