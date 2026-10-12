from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_balance import TransferBalance, TransferBalanceDict


class TransferBalanceGetResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/balance/get``"""

    balance: TransferBalance
    """Information about the balance held with Plaid."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferBalanceGetResponseDict(TypedDict):
    balance: TransferBalanceDict
    request_id: str
