from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer import Transfer, TransferDict


class TransferGetResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/get``"""

    transfer: Transfer
    """Represents a transfer within the Transfers API."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferGetResponseDict(TypedDict):
    transfer: TransferDict
    request_id: str
