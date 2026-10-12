from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class PaymentInitiationPaymentListRequest(SdkBaseModel):
    """PaymentInitiationPaymentListRequest defines the request schema for ``/payment_initiation/payment/list``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    count: int | None = 10
    """The maximum number of payments to return. If ``count`` is not specified, a maximum of 10 payments will be
    returned, beginning with the most recent payment before the cursor (if specified)."""

    cursor: OptionalNullable[RFC3339DateTime] = UNSET
    """A string in RFC 3339 format (i.e. "2019-12-06T22:35:49Z"). Only payments created before the cursor will be
    returned."""

    consent_id: OptionalNullable[str] = UNSET
    """The consent ID. If specified, only payments, executed using this consent, will be returned."""


class PaymentInitiationPaymentListRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    count: NotRequired[int | None]
    cursor: NotRequired[RFC3339DateTime | None]
    consent_id: NotRequired[str | None]
