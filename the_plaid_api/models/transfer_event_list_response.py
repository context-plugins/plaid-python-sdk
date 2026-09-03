from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_event import TransferEvent, TransferEventDict


class TransferEventListResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/event/list``"""

    transfer_events: list[TransferEvent]
    has_more: bool
    """Whether there are more events to be pulled from the endpoint that have not already been returned"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferEventListResponseDict(TypedDict):
    transfer_events: list[TransferEvent | TransferEventDict]
    has_more: bool
    request_id: str
