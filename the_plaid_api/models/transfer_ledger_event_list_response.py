from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_ledger_event import TransferLedgerEvent, TransferLedgerEventDict


class TransferLedgerEventListResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/ledger/event/list``"""

    ledger_events: list[TransferLedgerEvent]
    has_more: bool
    """Whether there are more events to be pulled from the endpoint that have not already been returned"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferLedgerEventListResponseDict(TypedDict):
    ledger_events: list[TransferLedgerEvent | TransferLedgerEventDict]
    has_more: bool
    request_id: str
