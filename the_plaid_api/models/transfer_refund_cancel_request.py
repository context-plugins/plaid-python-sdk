from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferRefundCancelRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/refund/cancel``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    refund_id: str
    """Plaid's unique identifier for a refund."""


class TransferRefundCancelRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    refund_id: str
