from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .wallet import Wallet, WalletDict


class WalletListResponse(SdkBaseModel):
    """WalletListResponse defines the response schema for ``/wallet/list``"""

    wallets: list[Wallet]
    """An array of e-wallets"""

    next_cursor: Optional[str] = UNSET
    """Cursor used for fetching e-wallets created before the latest e-wallet provided in this response"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class WalletListResponseDict(TypedDict):
    wallets: list[Wallet | WalletDict]
    next_cursor: NotRequired[str]
    request_id: str
