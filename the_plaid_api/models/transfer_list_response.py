from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer import Transfer, TransferDict


class TransferListResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/list``"""

    transfers: list[Transfer]
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferListResponseDict(TypedDict):
    transfers: list[TransferDict]
    request_id: str
