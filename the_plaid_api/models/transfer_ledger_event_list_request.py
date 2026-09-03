from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.ledger_event_source_type import LedgerEventSourceTypeOrStr


class TransferLedgerEventListRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/ledger/event/list``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    originator_client_id: OptionalNullable[str] = UNSET
    """Filter transfer events to only those with the specified originator client. (This field is specifically for
    resellers. Caller's client ID will be used if this field is not specified.)"""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    start_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The start created datetime of transfers to list. This should be in RFC 3339 format (i.e. 2019-12-06T22:35:49Z)"""

    end_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The end created datetime of transfers to list. This should be in RFC 3339 format (i.e. 2019-12-06T22:35:49Z)"""

    ledger_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for a Plaid Ledger Balance."""

    ledger_event_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for the ledger event."""

    source_type: OptionalNullable[LedgerEventSourceTypeOrStr] = UNSET
    """Source of the ledger event.

    ``"TRANSFER"`` - The source of the ledger event is a transfer ``"SWEEP"`` - The source of the ledger event is a
    sweep ``"REFUND"`` - The source of the ledger event is a refund"""

    source_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for a transfer, sweep, or refund."""

    count: OptionalNullable[int] = UNSET
    """The maximum number of transfer events to return. If the number of events matching the above parameters is greater
    than ``count``, the most recent events will be returned."""

    offset: OptionalNullable[int] = UNSET
    """The offset into the list of transfer events. When ``count``=25 and ``offset``=0, the first 25 events will be
    returned. When ``count``=25 and ``offset``=25, the next 25 events will be returned."""


class TransferLedgerEventListRequestDict(TypedDict):
    client_id: NotRequired[str]
    originator_client_id: NotRequired[str | None]
    secret: NotRequired[str]
    start_date: NotRequired[RFC3339DateTime | None]
    end_date: NotRequired[RFC3339DateTime | None]
    ledger_id: NotRequired[str | None]
    ledger_event_id: NotRequired[str | None]
    source_type: NotRequired[LedgerEventSourceTypeOrStr | None]
    source_id: NotRequired[str | None]
    count: NotRequired[int | None]
    offset: NotRequired[int | None]
