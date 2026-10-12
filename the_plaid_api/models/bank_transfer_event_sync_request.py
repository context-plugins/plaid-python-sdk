from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BankTransferEventSyncRequest(SdkBaseModel):
    """Defines the request schema for ``/bank_transfer/event/sync``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    after_id: int
    """The latest (largest) ``event_id`` fetched via the sync endpoint, or 0 initially."""

    count: int | None = 25
    """The maximum number of bank transfer events to return."""


class BankTransferEventSyncRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    after_id: int
    count: NotRequired[int | None]
