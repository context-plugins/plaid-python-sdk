from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_intent_get import TransferIntentGet, TransferIntentGetDict


class TransferIntentGetResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/intent/get``"""

    transfer_intent: TransferIntentGet
    """Represents a transfer intent within Transfer UI."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferIntentGetResponseDict(TypedDict):
    transfer_intent: TransferIntentGetDict
    request_id: str
