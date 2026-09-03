from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WalletTransactionCounterpartyBacs(SdkBaseModel):
    """The account number and sort code of the counterparty's account"""

    account: Optional[str] = UNSET
    """The account number of the account. Maximum of 10 characters."""

    sort_code: Optional[str] = UNSET
    """The 6-character sort code of the account."""


class WalletTransactionCounterpartyBacsDict(TypedDict):
    account: NotRequired[str]
    sort_code: NotRequired[str]
