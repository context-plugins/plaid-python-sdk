from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer import Transfer, TransferDict


class TransferCreateResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/create``"""

    transfer: Transfer
    """Represents a transfer within the Transfers API."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferCreateResponseDict(TypedDict):
    transfer: TransferDict
    request_id: str
