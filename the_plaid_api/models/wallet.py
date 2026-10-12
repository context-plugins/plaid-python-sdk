from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.wallet_status import WalletStatusOrStr
from .wallet_balance import WalletBalance, WalletBalanceDict
from .wallet_numbers import WalletNumbers, WalletNumbersDict


class Wallet(SdkBaseModel):
    """An object representing the e-wallet"""

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


class WalletDict(TypedDict):
    wallet_id: str
    balance: WalletBalanceDict
    numbers: WalletNumbersDict
    recipient_id: NotRequired[str]
    status: WalletStatusOrStr
