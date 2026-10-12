from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bank_transfer_event import BankTransferEvent, BankTransferEventDict


class BankTransferEventSyncResponse(SdkBaseModel):
    """Defines the response schema for ``/bank_transfer/event/sync``"""

    bank_transfer_events: list[BankTransferEvent]
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class BankTransferEventSyncResponseDict(TypedDict):
    bank_transfer_events: list[BankTransferEventDict]
    request_id: str
