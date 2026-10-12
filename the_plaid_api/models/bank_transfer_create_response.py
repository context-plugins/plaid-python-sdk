from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bank_transfer import BankTransfer, BankTransferDict


class BankTransferCreateResponse(SdkBaseModel):
    """Defines the response schema for ``/bank_transfer/create``"""

    bank_transfer: BankTransfer
    """Represents a bank transfer within the Bank Transfers API."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class BankTransferCreateResponseDict(TypedDict):
    bank_transfer: BankTransferDict
    request_id: str
