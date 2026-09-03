from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .wallet_transaction import WalletTransaction, WalletTransactionDict


class WalletTransactionListResponse(SdkBaseModel):
    """WalletTransactionListResponse defines the response schema for ``/wallet/transaction/list``"""

    transactions: list[WalletTransaction]
    """An array of transactions of an e-wallet, associated with the given ``wallet_id``"""

    next_cursor: Optional[str] = UNSET
    """The value that, when used as the optional ``cursor`` parameter to ``/wallet/transaction/list``, will return the
    corresponding transaction as its first entry."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class WalletTransactionListResponseDict(TypedDict):
    transactions: list[WalletTransaction | WalletTransactionDict]
    next_cursor: NotRequired[str]
    request_id: str
