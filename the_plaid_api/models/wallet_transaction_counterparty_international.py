from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WalletTransactionCounterpartyInternational(SdkBaseModel):
    """International Bank Account Number for a Wallet Transaction"""

    iban: Optional[str] = UNSET
    """International Bank Account Number (IBAN)."""


class WalletTransactionCounterpartyInternationalDict(TypedDict):
    iban: NotRequired[str]
