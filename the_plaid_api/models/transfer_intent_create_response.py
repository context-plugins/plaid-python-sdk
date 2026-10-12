from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_intent_create import TransferIntentCreate, TransferIntentCreateDict


class TransferIntentCreateResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/intent/create``"""

    transfer_intent: TransferIntentCreate
    """Represents a transfer intent within Transfer UI."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferIntentCreateResponseDict(TypedDict):
    transfer_intent: TransferIntentCreateDict
    request_id: str
