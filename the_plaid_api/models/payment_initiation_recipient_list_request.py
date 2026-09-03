from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PaymentInitiationRecipientListRequest(SdkBaseModel):
    """PaymentInitiationRecipientListRequest defines the request schema for ``/payment_initiation/recipient/list``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    count: OptionalNullable[int] = UNSET
    """The maximum number of recipients to return. If ``count`` is not specified, a maximum of 100 recipients will be
    returned, beginning with the recipient at the cursor (if specified)."""

    cursor: Optional[str] = UNSET
    """A value representing the latest recipient to be included in the response. Set this from ``next_cursor`` received
    from the previous ``/payment_initiation/recipient/list`` request. If provided, the response will only contain that
    recipient and recipients created before it. If omitted, the response will contain recipients starting from the most
    recent, and in descending order by the ``created_at`` time."""


class PaymentInitiationRecipientListRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    count: NotRequired[int | None]
    cursor: NotRequired[str]
