from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.wallet_status import WalletStatusOrStr
from .wallet_balance import WalletBalance, WalletBalanceDict
from .wallet_numbers import WalletNumbers, WalletNumbersDict


class WalletCreateResponse(SdkBaseModel):
    """WalletCreateResponse defines the response schema for ``/wallet/create``"""

    wallet_id: str
    """A unique ID identifying the e-wallet"""

    balance: WalletBalance
    """An object representing the e-wallet balance"""

    numbers: WalletNumbers
    """An object representing the e-wallet account numbers"""

    recipient_id: Optional[str] = UNSET
    """The ID of the recipient that corresponds to the e-wallet account numbers"""

    status: WalletStatusOrStr
    """The status of the wallet.

    ``UNKNOWN``: The wallet status is unknown.

    ``ACTIVE``: The wallet is active and ready to send money to and receive money from.

    ``CLOSED``: The wallet is closed. Any transactions made to or from this wallet will error."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class WalletCreateResponseDict(TypedDict):
    wallet_id: str
    balance: WalletBalance | WalletBalanceDict
    numbers: WalletNumbers | WalletNumbersDict
    recipient_id: NotRequired[str]
    status: WalletStatusOrStr
    request_id: str
