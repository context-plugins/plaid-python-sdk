from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bank_transfer import BankTransfer, BankTransferDict


class BankTransferListResponse(SdkBaseModel):
    """Defines the response schema for ``/bank_transfer/list``"""

    bank_transfers: list[BankTransfer]
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class BankTransferListResponseDict(TypedDict):
    bank_transfers: list[BankTransferDict]
    request_id: str
